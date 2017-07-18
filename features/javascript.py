import requests
import json
from bs4 import BeautifulSoup
from fingerprint import Fingerprint
import re

def fingerprint_function(url):
        f = Fingerprint(kgram_len=4, window_len=1, base=10, modulo=1000)
        print f.generate(str=url)

def extract_javascript_content(url):
    content=''
    r = requests.get(url, headers={'Connection': 'close'})
    soup = BeautifulSoup(r.content,'lxml')
    data=soup.find('script')
    try:
        content=content+data.text
    except:
        pass
    try:
        src = [sc["src"] for sc in soup.find_all("script",src=True)]
        for i in src:
            if ('http:' in i) or ('https:' in i):
                r=requests.get(i)
                content=content+r.text
            else:
                r = requests.get('http:'+i)
                content=content+r.text
    except:
        pass
    return content
print extract_javascript_content("https://aviary.com/home")

def strings_in_javascript(url):
    content=extract_javascript_content(url)
    #Strings with single quote.
    print "Single quote strings."
    print re.findall("'([^']*)'", content)
    #Strings with double quotes.
    print "double quote strings."
    print re.findall('"([^"]*)"', content)
strings_in_javascript("https://aviary.com/home")
def script_in_chars(url):
    content=extract_javascript_content(url)
    return len(content)

def count_function(name,url):
    content=extract_javascript_content(url)
    return content.count(name)

def eval_count(url):
    return count_function('eval',url)

def setInterval_count(url):
    return count_function('setInterval',url)

def setTimeout_count(url):
    return count_function('setTimeout',url)
#print check_function('getTime',"http://google.com")
