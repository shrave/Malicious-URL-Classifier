import urllib2
import urllib
from xml.dom import minidom
import csv
import pygeoip,requests
from bs4 import BeautifulSoup
import re
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

nf=-1
'''def web_content_features(url):
    wfeatures={}
    total_cnt=0
    try:
        source_code = str(opener.open(url))
        #print source_code[:500]

        wfeatures['src_html_cnt']=source_code.count('<html')
        wfeatures['src_hlink_cnt']=source_code.count('<a href=')
        wfeatures['src_iframe_cnt']=source_code.count('<iframe')
        wfeatures['src_applet_cnt']=source_code.count('<applet')
        wfeatures['src_src_cnt']=source_code.count('<src')
        wfeatures['src_script_cnt']=source_code.count('<script')
        wfeatures['src_embed_cnt']=source_code.count('<embed')
        wfeatures['src_meta_cnt']=source_code.count('<meta')
        #suspicioussrc_ javascript functions count

        wfeatures['src_eval_cnt']=source_code.count('eval(')
        wfeatures['src_escape_cnt']=source_code.count('escape(')
        #wfeatures['src_link_cnt']=source_code.count('link(')
        #wfeatures['src_underescape_cnt']=source_code.count('underescape(')
        #wfeatures['src_exec_cnt']=source_code.count('exec(')
        #wfeatures['src_search_cnt']=source_code.count('search(')
        wfeatures['src_timeout_cnt']=source_code.count('<setTimeOut(')
        wfeatures['src_setinterval_cnt']=source_code.count('<setInterval(')
        for key in wfeatures:
            if(key!='src_html_cnt' and key!='src_hlink_cnt' and key!='src_iframe_cnt'):
                total_cnt+=wfeatures[key]
        wfeatures['src_total_jfun_cnt']=total_cnt

    except Exception, e:
        print "Error"+str(e)+" in downloading page "+url
        default_val=nf

        wfeatures['src_html_cnt']=default_val
        wfeatures['src_hlink_cnt']=default_val
        wfeatures['src_iframe_cnt']=default_val
        wfeatures['src_eval_cnt']=default_val
        wfeatures['src_escape_cnt']=default_val
        #wfeatures['src_link_cnt']=default_val
        #wfeatures['src_underescape_cnt']=default_val
        #wfeatures['src_exec_cnt']=default_val
        #wfeatures['src_search_cnt']=default_val
        wfeatures['src_timeout_cnt']=default_val
        wfeatures['src_setinterval_cnt']=default_val
        wfeatures['src_total_jfun_cnt']=default_val
        wfeatures['src_src_cnt']=default_val
        wfeatures['src_script_cnt']=default_val
        wfeatures['src_embed_cnt']=default_val
        wfeatures['src_meta_cnt']=default_val

    return wfeatures'''
def content_features_count(url,tag):
    soup=get_page_content(url)
    return len(soup.findAll(tag))

def redirect_check(url):
    r = requests.get(url)
    if len(r.history)<=1 or url.count('//')==0:
        return False
    else:
        return True
def header_response(url):
    page = urllib2.urlopen(url)
    l=page.info().headers
    d={}
    d['Content-Type']=l[0].split('Content-Type: ')[1][:-2]
    d['Server']=l[1].split('Server: ')[1][:-2]
    d['X-Powered-By']=l[2].split('X-Powered-By: ')[1][:-2]
    d['Date']=l[3].split('Date: ')[1][:-2]
    d['Connection']=l[4].split('Connection: ')[1][:-2]
    d['Content-Length']=l[5].split('Content-Length: ')[1][:-2]
    return d

def get_page_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def hyperlink_count(url):
    website=urllib2.urlopen(url)
    html = website.read()
    links = len(re.findall('"((http|ftp)s?://.*?)"', html))
    return links

def external_javascript_file(url):
    soup=get_page_content(url)
    src = [sc["src"] for sc in soup.find_all("script",src=True)]
    return len(src)
