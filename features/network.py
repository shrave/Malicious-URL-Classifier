import requests
def redirect_count_with_warning(url):
    r = requests.get(url)
    return (r.history)
    #Number of redirects.
def redirect_count_total(url):
    r=urllib2.urlopen('https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url='+url+ '&filter_third_party_resources=true&locale=en_US&screenshot=false&strategy=desktop&key=AIzaSyDa2L0i-oPVgsry9HlW5R7BLpDTL9b0Oz8')
    data=json.load(r)
    #Number of landing page redirects.

def download_packet_length(url):
    response = requests.get(url)
    return len(response.content)

print redirect_count_with_warning('http://utility.baidu.com/traf/click.php?id=215&url=https://log0.wordpress.com')

import ssl, socket

hostname = 'google.com'
ctx = ssl.create_default_context()
s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
s.connect((hostname, 443))
cert = s.getpeercert()

subject = dict(x[0] for x in cert['subject'])
issued_to = subject['commonName']
issuer = dict(x[0] for x in cert['issuer'])
issued_by = issuer['commonName']
