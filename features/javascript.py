import requests
import json
from bs4 import BeautifulSoup
from fingerprint import Fingerprint
import re
import unicodedata
import math

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

def strings_in_javascript(url):
    content=extract_javascript_content(url)
    strings1= re.findall("'([^']*)'", content)
    strings2= re.findall('"([^"]*)"', content)
    java_string=[]
    for i in strings2+strings1:
        if i:
            java_string.append(unicodedata.normalize('NFKD', i).encode('ascii','ignore'))
    return java_string

def entropy(string):
        "Calculates the Shannon entropy of a string"
        prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]
        entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])
        return entropy

def entropy_of_strings(url):
    strings=strings_in_javascript(url)
    ent=[]
    for i in strings:
        ent.append(entropy(i))
    return ent

def length_of_strings(url):
    strings=strings_in_javascript(url)
    arr=[]
    arr=map(len,strings)
    return arr

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
