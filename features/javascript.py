import requests
import json
from bs4 import BeautifulSoup
from fingerprint import Fingerprint
import re
import unicodedata
import math
from slimit.lexer import Lexer
from useful_methods import average
from pyjsparser import PyJsParser

dom_list=['querySelector','querySelectorAll','addEventListener','removeEventListener',
'appendChild','removeChild','replaceChild','cloneNode','insertBefore','createDocumentFragment'
'getComputedStyle','setAttribute','getAttribute','removeAttribute']

obfuscation_list=['concat','split','replace','encode','fromCharCode','unescape','substring']

event_trigger_list=['onerror',  'onload',  'onunload', 'onbeforeload', 'onbeforeunload',
'onmouseover', 'addEventListener','attachEvent','dispatchEvent','fireEvent']

suspicious_list=['Math.random','insertBefore','ActiveXObject','innerHTML', 'Ajax','navigator']
#Update lists if required to improve performance.

def fingerprint_function(url):
        f = Fingerprint(kgram_len=4, window_len=1, base=10, modulo=1000)
        return f.generate(str=url)

def one_line_code(url):
    content=''
    r = requests.get(url, headers={'Connection': 'close'})
    soup = BeautifulSoup(r.content,'lxml')
    data=soup.find('script')
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
    content_list=content.split('\n')
    if len(content_list)>1 or content == '':
        return 0
    return 1

print one_line_code('https://ravindrababuravula.com/gatexcel80.php')

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

def avg_line_length_script(url):
    script=extract_javascript_content(url)
    line_list=script.split('\n')
    lengths = [len(i) for i in line_list]
    return 0 if len(lengths) == 0 else (float(sum(lengths)) / len(lengths))


def whitespace_script(url):
    script=extract_javascript_content(url)
    for i in script:
        if i is ' ':
            count=count+1
    return float(count)/float(len(script))

def strings_in_javascript(url):
    content=extract_javascript_content(url)
    string_list=content.split('var')
    print string_list
    strings1= re.findall("'([^']*)'", content)
    strings2= re.findall('"([^"]*)"', content)
    java_string=[]
    for i in strings2:
        if i:
            java_string.append(unicodedata.normalize('NFKD', i).encode('ascii','ignore'))
    for i in strings1:
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

def average_length_string(url):
    len_list=length_of_strings(url)
    return float(sum(len_list))/len(len_list)

def string_with_iframe(url):
    strings=strings_in_javascript(url)
    count=0
    for i in strings:
        if 'iframe' in i:
            count=count+1
    return count

def script_in_chars(url):
    content=extract_javascript_content(url)
    return len(content)

def count_function(name,url):
    content=extract_javascript_content(url)
    return content.count(name)

def eval_count(url):
    return count_function('eval',url)
#print eval_count("http://www.toolani.de/")

def setInterval_count(url):
    return count_function('setInterval',url)

def setTimeout_count(url):
    return count_function('setTimeout',url)

def variables_functions_in_script(url):
    js=extract_javascript_content(url)
    identifiers = []
    lexer = Lexer()
    lexer.input(js)
    for token in lexer:
        if token.type == 'ID':
            identifiers.append(unicodedata.normalize('NFKD', token.value).encode('ascii','ignore'))
    return identifiers

def obfuscation_functions(url):
    count=0
    var_list=list(set(variables_functions_in_script(url)))
    for word in var_list:
        if word in obfuscation_list:
            count=count+1
    return count

def event_trigger_functions(url):
    count=0
    var_list=list(set(variables_functions_in_script(url)))
    for word in var_list:
        if word in event_trigger_list:
            count=count+1
    return count

def suspicious_strings_functions(url):
    count=0
    var_list=list(set(variables_functions_in_script(url)))
    for word in var_list:
        if word in suspicious_list:
            count=count+1
    return count

def dom_modification(url):
    count=0
    var_list=list(set(variables_functions_in_script(url)))
    for word in var_list:
        if word in dom_list:
            count=count+1
    return count

def long_variables_functions(url):
    var_list=variables_functions_in_script(url)
    len_list=[]
    for k in var_list:
        if len(k)>=35:
            len_list.append(len(k))
    return len(len_list)
    #long to be >35
#print dom_modification("http://www.toolani.de/")
#count=0
#for i in dom_list:
#        count=count+count_function(i,"http://www.toolani.de/")
#print count
