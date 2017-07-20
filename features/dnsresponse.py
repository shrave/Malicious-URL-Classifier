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
#Whois registration info.
def whoisinfo(url):
    return whois.whois(url)

def PTR(url):
    #addr = reversename.from_address(IP(url))
    addr=DNS_response(url)
    import dns.resolver
    myResolver = dns.resolver.Resolver()
    myAnswers = myResolver.query("3.125.194.174.in-addr.arpa", "PTR")
    return myAnswers
    name, alias, addresslist = socket.gethostbyaddr(IP(url))

def DNS_response(url):
    import dns.resolver
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
    
def location(url):
    if (DNS_response(url)):
        my_ip=(DNS_response(url))
        return ipapi.location(ip=my_ip[0], key=None, field=None)
#print IP_Location('http://www.sinduscongoias.com.br/index.html')
#print DNS_response('www.setchon.com/jd/upload.aspx')
#print PTR('http://www.sinduscongoias.com.br/index.html')
#print whoisinfo('http://www.sinduscongoias.com.br/index.html')
#print location('amazon.in')
#country code, netspeed,region,timezone.
#print ASN('amazon.in')
