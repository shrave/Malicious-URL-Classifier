import requests
def redirect_count(url):
    r = requests.get(url)
    return len(r.history)-1
