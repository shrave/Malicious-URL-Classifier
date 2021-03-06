import validators
import collections
import urllib2
import urllib
from xml.dom import minidom
import csv
from urlparse import urlparse
import pygeoip,requests
from bs4 import BeautifulSoup
import re
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
from urlparse import urlparse
from os.path import splitext
from useful_methods import *
import mechanize
from time import sleep
from dnsresponse import domain_name
nf=-1

double_doc_list=['html','head','title','body']
filetypes_list=[".gif",".jpg",".png",".cgi",".pl",".js",".png",".png",".png"]

def char_count(url):
    url = 'http://' + url
    response = requests.get(url)
    return len(response.text)

def redirect_check(url):
    url = 'http://' + url
    r = requests.get(url)
    if len(r.history)<=1 or url.count('//')==0:
        return 0
    else:
        return 1

def header_response(url):
    url = "http://" + url
    page = urllib2.urlopen(url)
    l=page.info().headers
    d={}
    for i in l:
        items = i.split(':')
        d[items[0]] = i.replace(items[0]+':',"")
    return d

def get_page_content(url):
    url = 'http://' + url
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup
#BeautifulSoup requires http:// at the begining of URL.

def tag_names(url):
    soup=get_page_content(url)
    taglist=[unicode_decode(tag.name) for tag in soup.find_all()]
    return taglist


def html_tag(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    taglist=[unicode_decode(tag.name) for tag in soup.find_all()]
    return taglist

def unknown_tags(url):
    html_tags=set(html_tag(url))
    all_tags=set(tag_names(url))
    return (all_tags - html_tags)

def hyperlink_list(url):
    url = 'http://' + url
    website=urllib2.urlopen(url)
    html = website.read()
    links = (re.findall('"((http|ftp)s?://.*?)"', html))
    links_list = []
    for i in links:
        links_list.append(i[0])
    return links_list

#print hyperlink_list('www.google.com')
def hyperlink_count(url):
    return len(hyperlink_list(url))
#print hyperlink_count('http://www.google.com')
def external_javascript_file_count(url):
    soup=get_page_content(url)
    src = [sc["src"] for sc in soup.find_all("script",src=True)]
    return len(src)

def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext

def script_with_wrong_ext(url):
    soup=get_page_content(url)
    try:
        src = [sc["src"] for sc in soup.find_all("script",src=True)]
        for i in src:
            if get_ext(i)!='.js':
                return 1
    except:
        return 0
    return 0

def page_title(url):
    soup=get_page_content(url)
    try:
        title=soup.title.string
        return title
    except:
        return

def page_title_length(url):
    name=page_title(url)
    if type(name)==None:
        return 0
    return len(name)

def whitespace_count(url):
    count=0
    soup=get_page_content(url)
    for i in soup:
        if i is ' ':
            count=count+1
    return count

def whitespace_percent(url):
    return float(whitespace_count(url))/float(char_count(url))

def visible(element):
    if element.parent.name in ['style', 'script', '[document]']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return 0
    return 1

def text_in_content(url):
    soup = get_page_content(url)
    data = soup.findAll(text=True)
    result = filter(visible, data)
    result=list(map(unicode_decode,result))
    return result

def suspicious_content_tag(url):
    text=text_in_content(url)
    #print text
    #We check if this content corresponds to a shell code by:
    #If longer than 128 chars and less than 5% whitespace.
    #Output is a count of tags with these huerisitics.
    susp_count=0
    for i in text:
        count=0
        if len(i)>128:
            for j in list(bool(not s or s.isspace()) for s in i):
                if j:
                    count=count+1
            if 1-(float(count)/float(len(i)))<=0.05:
                susp_count=susp_count+1
    return susp_count

def double_documents(url):
    count=0
    for tag in double_doc_list:
        if content_features_count(url,tag)>=2:
            count=count+1
    return count

def downloadlink(l):
    br.click_link(l)
    return br.response().info()['Content-Length']

def file_sizes_per_extension(url,filetype):
    filetypes=[]
    filetypes.append(filetype)
    filesizes=[]
    br = mechanize.Browser()
    br.set_handle_robots(False)
    url = 'http://' + url
    br.open(url)
    f=open("source.html","w")
    f.write(br.response().read())
    myfiles=[]
    for l in br.links():
        for t in filetypes:
            if t in str(l):
                myfiles.append(l)
    for l in myfiles:
        sleep(1) #throttle so you dont hammer the site
        filesizes.append(downloadlink(l))
    if filesizes:
        return (min(filesizes),max(filesizes),average(filesizes))
    else:
        return (0,0,0)

def max_min_avg_file_extensions(url):
    file_ext_list=[]
    for i in filetypes_list:
        file_ext_list.append(file_sizes_per_extension(url,i))
    return file_ext_list

def content_features_count(url,tag):
    soup=get_page_content(url)
    return len(soup.findAll(tag))

def content_features_attribute_count(url,tag,attribute):
    soup=get_page_content(url)
    return len(soup.findAll(tag, attrs = {attribute : True}))

#A tuple having same orign links and different origin links.
#Combination of hostname, URI scheme and port number. They should match.

def same_different_origin_count(url):
    links=hyperlink_list(url)
    origin_info=[]
    for i in links:
        o=urlparse(i)
        origin_info.append((o.scheme,o.hostname,o.port))
    '''counter=collections.Counter(origin_info)
    different_origin=counter.values.count(1)'''
    different_origin=list(set(origin_info))
    #unique origins
    same_origin_count=len(origin_info)-len(different_origin)
    return (same_origin_count,len(different_origin) )

#print same_different_origin_count('www.google.com')
def origin_details(url):
    o=urlparse(url)
    return (o.scheme,o.hostname,o.property,o.port)

def source_in_other_domain(url):
    soup=get_page_content(url)
    source_list=[]
    count=0
    sources=soup.find_all(attrs={"src":True})
    for source in sources:
        if validators.url(source['src']):
            source_list.append(source['src'])
    for link in source_list:
        if domain_name(link)!=domain_name(url):
            count=count+1
    return count
    #All the elements having different domain.

def line_count(url):
    url = 'http://' + url
    r = requests.get(url, stream = True)
    count=0
    for i in r.iter_lines():
        if i:
            count=count+1
    return count

def web_page_size(url):
    url = 'http://' + url
    try:
        response = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        print e.code
    except urllib2URLError, e:
        print e.args
    return len(response.read())

def script_percentage(url):
    soup =  get_page_content(url)
    text = soup.findAll('script')
    url = 'http://' + url
    response = requests.get(url)
    scr = response.content
    count = 0
    coun1 = 0
    for i in scr:
        count = count + 1
    text = str(text)
    for i in text:
        coun1 = coun1 + 1
    return (float(coun1)/float(count))*100

delimiter_list= ["/", "?", ".", "=", "-","_"]
def delimiter_count(url):
    count = 0
    for i in delimiter_list:
        if i in url:
            count = count + 1
    return count
