import re
import ssl, socket
import requests
from dnsresponse import host
from useful_methods import unicode_decode
from tld import get_tld
from lexical import subdomain_name
import urllib2
import urllib
import json

def redirect_count_with_warning(url):
    url = 'http://' + url
    r = requests.get(url)
    return (r.history)
    #Number of redirects.
def redirect_count_total(url):
    url = 'http://' + url + '/'
    r=urllib2.urlopen('https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url='+url+ '&filter_third_party_resources=true&locale=en_US&screenshot=false&strategy=desktop&key=AIzaSyDa2L0i-oPVgsry9HlW5R7BLpDTL9b0Oz8')
    data=json.load(r)
    #Number of landing page redirects.

def download_packet_length(url):
    response = requests.get(url)
    return len(response.content)

def certificate(url):
    url = 'http://' + url
    hostname = host(url)
    print hostname
    ctx = ssl.create_default_context()
    s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
    s.connect((hostname, 443))
    cert = s.getpeercert()
#    for i in cert.keys():
#        print cert[i]
    return cert
    #Returns a dict/json of all info about the cert and issuer.
    #Modify and convert all unicodes to strings.

#print certificate('www.google.com')
def start_end_cert(url):
    cert=certificate(url)
    start_date = cert['notBefore']
    end_date=cert['notAfter']
    return (unicode_decode(start_date),(end_date))

def host_components_count(url):
    url = 'http://' + url
    name=host(url)
    return (re.findall(r"[\w']+", name))
#print host_components_count('www.google.com')

def details_CA_issuer(url):
    cert=certificate(url)
    issuer = dict(x[0] for x in cert['issuer'])
    issuer_details={}
    issuer_details['issued_by'] = issuer['commonName']
    issuer_details['organisationName']=issuer['organisationName']
    issuer_details['organisationalUnitname']=issuer['organizationalUnitName']
    issuer_details['countryName']=issuer['countryName']
    return issuer_details

def TLD_presence(url):
    if get_tld(url, fix_protocol=True,fail_silently=True):
        return 1
    return 0

def subdomain_presence(url):
    if subdomain_name(url):
        return 1
    return 0
