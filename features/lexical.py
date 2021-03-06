import socket
import ipaddress
import tldextract
from urlparse import parse_qs
from urlparse import urlparse
from posixpath import basename, dirname
import urlparse
from useful_methods import unicode_decode
import re
from glob import glob
from dnsresponse import hostname

f=open('blacklists.txt', 'r')
black_list=f.read().split()
for word in black_list:
    if type(word) != str:
        word=unicode_decode(word)
delim=['-','.','_','~',':','/','?','#','[',']','@','!','$','&,''','(',')','*','+',',',';','=','`','.']
#The list of delimiters used in the analyses.
def url_length(url):
    return len(url)

def special_chars(url):
    count=0
    for i in url:
        if not i.isalnum():
                count=count+1
    return count

def ratio_special_chars(url):
    count=special_chars(url)
    return float(count)/float(len(url))

def token_count(url):
    return len(getTokens(url))

def Presence_of_IP(url):
    tokens_words=getTokens(url)
    #print tokens_words
    cnt=0;
    for ele in tokens_words:
        try:
            ele =unicode(ele, "utf-8")
            ip = ipaddress.ip_address(ele)
            cnt=cnt+1
        except:
            pass
    if cnt>0:
        return 1
    return 0

def getTokens(url):
    return re.split('\W+',url)

def suspicious_word_count(url):
    tokens_words=getTokens(url)
    sec_sen_words=['confirm', 'account', 'banking', 'secure', 'ebayisapi', 'webscr', 'login', 'signin']
    cnt=0
    for ele in sec_sen_words:
        if(ele in tokens_words):
            cnt+=1;
    return cnt

def domain_name(url):
    return tldextract.extract(url).domain

def subdomain_name(url):
    return tldextract.extract(url).subdomain

def subdomain_length(url):
    return len(subdomain_name(url))

def domain_token_count(url):
    return token_count(domain_name(url))

def longest_domain_token_count(url):
    return max(getTokens(url))

def query_variables_count(url):
    return len(parse_qs(urlparse.urlparse(url).query, keep_blank_values=True))

def max_length_variable(url):
    k=(parse_qs(urlparse.urlparse(url).query, keep_blank_values=True))
    if k.keys():
        return max(len(w) for w in k.keys() if w)
    return 0
####Other functions.
def countdelim(url):
    count = 0
    for each in url:
        if each in delim:
            count = count + 1
    return count
#Suspicious_TLD=['zip','cricket','link','work','party','gq','kim','country','science','tk']
#Suspicious_Domain=['luckytime.co.kr','mattfoll.eu.interia.pl','trafficholder.com','dl.baixaki.com.br','bembed.redtube.comr','tags.expo9.exponential.com','deepspacer.com','funad.co.kr','trafficconverter.biz']
def countSubDomain(subdomain):
    if not subdomain:
        return 0
    else:
        return len(subdomain.split('.'))
def alphabet_count(url):
    return sum(c.isalpha() for c in url)

def digit_count(url):
    return sum(c.isdigit() for c in url)

def countQueries(query):
    if not query:
        return 0
    else:
        return len(query.split('&'))

def countdots(url):
    return url.count('.')

def count_at_symbol(url):
    return url.count('@')+url.count('-')

#These are the key value pairs of the argument in the URL.
def key_value_pairs(url):
    return dict(urlparse.parse_qs(urlparse.urlsplit(url).query))

def argument_length(url):
    return len(urlparse.urlsplit(url).query)

def isPresentHyphen(url):
    return url.count('-')

def isPresentAt(url):
    return url.count('@')

#Sub-directory count.
def countSubDir(url):
    return url.count('/')

def get_ext(url):
    """Return the filename extension from url, or ''."""

    root, ext = splitext(url)
    return ext

def get_filename(url):
    root, ext = splitext(url)
    return root

def URL_path(url):
    parse_object = urlparse.urlparse(url)
    return parse_object.path

def URL_scheme(url):
    parse_object = urlparse.urlparse(url)
    return parse_object.scheme

def scheme_http_or_not(url):
    if URL_scheme(url)=='http' or URL_scheme(url)=='https':
        return 1
    return 0

def path_length(url):
    return len(URL_path(url))

def directory_length(url):
    return len(dirname(URL_path(url)))

def sub_directory(url):
    path=URL_path(url)
    dirname_path=dirname(URL_path(url))
    path=path.replace(dirname_path, '')
    return path

def sub_directory_special_count(url):
    count=0
    sub_path=sub_directory(url).strip("/")
    for lim in delim:
        if lim in sub_path:
            count=count+sub_path.count(lim)
    return count

def sub_directory_tokens_count(url):
    path= sub_directory(url)
    tokens=re.split('\W+',path)
    tokens = filter(None, tokens)
    return len(tokens)

def filename(url):
    filename=basename(URL_path(url))
    return (filename.split('.')[0])

def filename_length(url):
    return len(filename(url))

def port_number(url):
    o=urlparse.urlparse(url)
    #print o.port
    if o.port != None:
        return 1
    return 0

#print port_number('www.google.com')
def blacklisted_word_present(url):
    for word in black_list:
        if word in url:
            return 1
    return 0

def longest_token_path(url):
    tokens=getTokens(URL_path(url))
    return max(len(w) for w in tokens)

def hyphens_instead_dots_domain(url):
    domain=domain_name(url)
    if domain.count('-')>domain.count('.'):
        return 1
    return 0

def hostname_unicode(url):
    host_name=hostname(url)
    if type(host_name) is unicode:
        return 1
    for s in host_name:
        if type(s) is unicode:
            return 1
    return 0

def another_char_hostname(url):
    host_name=hostname(url)
    #print host_name
    char='.'
    for dl in delim:
        if (host_name.count(dl))>host_name.count(char):
            if dl!='.':
                char=dl
    if char=='.':
        return 0
    return 1
