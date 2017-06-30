import pyasn,socket
from urlparse import urlparse
from ipwhois import IPWhois
import whois
from dns import resolver
from dns import reversename
from urllib2 import urlopen
from contextlib import closing
import json

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

def ASN():
    return results['asn']
#Whois registration info.
def whoisinfo(url):
    return whois.whois(url)
def PTR(url):
    addr = reversename.from_address(IP(url))
    return resolver.query(addr, "PTR")[0]
    name, alias, addresslist = socket.gethostbyaddr(IP(url))
    #return name
def DNS_response(url):
    return addrs = [ str(i[4][0]) for i in socket.getaddrinfo(name, 80) ]
    #All IPS Adresses reolved list.
def IP_Location(url):
    try:
    with closing(urlopen(url)) as response:
        location = json.loads(response.read())
        return location
        location_city = location['city']
        location_state = location['region_name']
        location_country = location['country_name']
        location_zip = location['zipcode']
