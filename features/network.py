import requests
def redirect_count_with_warning(url):
    r = requests.get(url)
    return (r.history)
    #Number of redirects.
def redirect_count_total(url):
    r=urllib2.urlopen('https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url='+url+ '&filter_third_party_resources=true&locale=en_US&screenshot=false&strategy=desktop&key=AIzaSyDa2L0i-oPVgsry9HlW5R7BLpDTL9b0Oz8')
    data=json.load(r)
    #Number of landing page redirects.


print redirect_count_with_warning('http://utility.baidu.com/traf/click.php?id=215&url=https://log0.wordpress.com')
