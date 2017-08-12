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
    #addr = reversename.from_address(IP(url))
    addr=DNS_response(url)
    import dns.resolver
    myResolver = dns.resolver.Resolver()
    myAnswers = myResolver.query("3.125.194.174.in-addr.arpa", "PTR")
    l=[]
    for rdata in myAnswers: #for each response
        l.append(str(rdata))
    return l
    name, alias, addresslist = socket.gethostbyaddr(IP(url))

def resolved_ip_count(url):
    return len(DNS_response(url))
#Name of nameserver.
def nameserver(url):
    myResolver = dns.resolver.Resolver()
    try:
        myAnswers = myResolver.query(url, "NS")
        l=[]
        for rdata in myAnswers: #for each response
            l.append(str(rdata))
        return l
    except:
        print "No IP resolved."

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
    try:
        myAnswers = myResolver.query(url, "A")
        l=[]
        for rdata in myAnswers: #for each response
            l.append(str(rdata))
        return l
    except:
        print "No IP resolved."
    #All IPS Adresses reolved list.

def mailserver(url):
    def DNS_response(url):
        myResolver = dns.resolver.Resolver()
        try:
            myAnswers = myResolver.query(url, "MX")
            l=[]
            for rdata in myAnswers: #for each response
                l.append(str(rdata))
            return l
        except:
            print "No IP resolved."
        #All IPS Adresses reolved list.
def location(url):
    if (DNS_response(url)):
        my_ip=(DNS_response(url))
        return convert_keys_to_string(ipapi.location(ip=my_ip[0], key=None, field=None))

#print IP_Location('http://www.sinduscongoias.com.br/index.html')
#print location('www.amazon.com')
#print PTR('http://www.sinduscongoias.com.br/index.html')
#print whoisinfo('http://www.sinduscongoias.com.br/index.html')
#print location('amazon.in')
#country code, netspeed,region,timezone.
#print ASN('amazon.in')
#print DNS_response('amazon.com')
#print nameserver('www.amazon.com')
#print WhoIS('www.amazon.com')
