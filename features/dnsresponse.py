import pyasn,socket
from urlparse import urlparse
from ipwhois import IPWhois
import whois
from dns import resolver
from dns import reversename
from urllib2 import urlopen
from contextlib import closing
import json
from json import load
import ipapi
import dns.resolver
'''' Inline imports'''
from useful_methods import convert_keys_to_string


results={}
def host(url):
    return urlparse(url).hostname

def IP(url):
    return socket.gethostbyname(url)

def WhoIS(url):
    results={}
    I=IP(url)
    obj = IPWhois(I)
    results = obj.lookup_rdap(depth=1)

def ASN(url):
    return whoisinfo(url)['asn']
def ASN_malicous(url):
    return #matching list in website see if malicious.
#Whois registration info.
def whoisinfo(url):
    return whois.whois(url)

def PTR(url):
    myResolver = dns.resolver.Resolver()
    myAnswers = myResolver.query("3.125.194.174.in-addr.arpa", "PTR")
    l=[]
    for rdata in myAnswers: #for each response
        l.append(str(rdata))
    return l
    name, alias, addresslist = socket.gethostbyaddr(IP(url))

def PTR_A_record(url):
    if set(map(IP,PTR(url))) & set(DNS_response(url)):
        return 1
    return 0

def same_ip(url):
    if set(map(IP,PTR(url))) & set(DNS_response(url)) & set(map(IP,mailserver(url))):
        return 1
    return 0

def resolved_ip_count(url):
    return len(DNS_response(url))

def nameserver(url):
    myResolver = dns.resolver.Resolver()
    try:
        myAnswers = myResolver.query(url, "NS")
        l=[]
        for rdata in myAnswers: #for each response
            l.append(str(rdata))
        return l
    except:
        pass

def nameserver_IP(url):
    namelist=nameserver(url)
    l=[]
    for name in namelist:
        if IP(url) not in l:
            l.append(IP(url))
    return l

def nameserver_count(url):
    return len(nameserver(url))
#Host IPs.
def DNS_response(url):
    myResolver = dns.resolver.Resolver()
    url=domain_name(url)
    print url
    try:
        myAnswers = myResolver.query(url, "A")
        l=[]
        for rdata in myAnswers: #for each response
            l.append(str(rdata))
        return l
    except:
        #print "No IP resolved."
        pass
    #All IPS Adresses reolved list.

def mailserver(url):
    myResolver = dns.resolver.Resolver()
    try:
        myAnswers = myResolver.query(url, "MX")
        l=[]
        for rdata in myAnswers: #for each response
            l.append(str(rdata))
        return l
    except:
        pass

def mailserver_IP(url):
    return set(map(IP,mailserver(url)))

def reverse_IP(url):
    ip=IP(url)
    rev_name = reversename.from_address(ip)
    reversed_dns = str(resolver.query(rev_name,"PTR")[0])
    return reversed_dns

#Dont put http.
def location(url):
    if (DNS_response(url)):
        my_ip=(DNS_response(url))
        return convert_keys_to_string(ipapi.location(ip=my_ip[0], key=None, field=None))
#Iterate through the my_ip list in ipapi.

#Rewrite proper function for it.
def remove_http(url):
     lines = lines.replace("http://","")
     lines = lines.replace("www.", "") # May replace some false positives ('www.com')
     urls = [url.split('/')[0] for url in lines.split()]
     return urls

def domain_name(url):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain

def origin_destination(url):
