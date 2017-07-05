import socket
import ipaddress

nf=-1
def url_length(url):
    return len(url)

def special_chars(url):
    count=0
    for i in url:
        if not i.isalnum():
                count=count+1
    return count

def ratio_special_chars(url):
    count=special_chars(url)
    return float(count)/float(len(url))

def getTokens(url):
	tokensBySlash = str(url.encode('utf-8')).split('/')	#get tokens after splitting by slash
	allTokens = []
	for i in tokensBySlash:
		tokens = str(i).split('-')	#get tokens after splitting by dash
		tokensByDot = []
		for j in range(0,len(tokens)):
			tempTokens = str(tokens[j]).split('.')	#get tokens after splitting by dot
			tokensByDot = tokensByDot + tempTokens
		allTokens = allTokens + tokens + tokensByDot
	allTokens = list(set(allTokens))	#remove redundant tokens
	if 'com' in allTokens:
		allTokens.remove('com')	#removing .com since it occurs a lot of times and it should not be included in our features
	return allTokens

#Code for average length, token count and max length token from given list.
'''        no_ele=sum_len=largest=0
        for ele in allTokens:
                l=len(ele)
                sum_len+=l
                if l>0:                                        ## for empty element exclusion in average length
                        no_ele+=1
                if largest<l:
                        largest=l
        try:
            return [float(sum_len)/no_ele,no_ele,largest]
        except:
            return [0,no_ele,largest]
'''
def Presence_of_IP(url):
    tokens_words=getTokens(url)
    #print tokens_words
    cnt=0;
    for ele in tokens_words:
        try:
            ele =unicode(ele, "utf-8")
            ip = ipaddress.ip_address(ele)
            cnt=cnt+1
        except:
            pass
    if cnt>0:
        return True
    return False

def bag_of_words(url):
    return re.split('\W+',url)

def suspicious_word_count(url):
    tokens_words=getTokens(url)
    sec_sen_words=['confirm', 'account', 'banking', 'secure', 'ebayisapi', 'webscr', 'login', 'signin']
    cnt=0
    for ele in sec_sen_words:
        if(ele in tokens_words):
            cnt+=1;
    return cnt

def countdelim(url):
    count = 0
    delim=[';','_','?','=','&']
    for each in url:
        if each in delim:
            count = count + 1

    return count
#Suspicious_TLD=['zip','cricket','link','work','party','gq','kim','country','science','tk']
#Suspicious_Domain=['luckytime.co.kr','mattfoll.eu.interia.pl','trafficholder.com','dl.baixaki.com.br','bembed.redtube.comr','tags.expo9.exponential.com','deepspacer.com','funad.co.kr','trafficconverter.biz']
def countSubDomain(subdomain):
    if not subdomain:
        return 0
    else:
        return len(subdomain.split('.'))

def countQueries(query):
    if not query:
        return 0
    else:
        return len(query.split('&'))

def countdots(url):
    return url.count('.')


def isPresentHyphen(url):
    return url.count('-')

def isPresentAt(url):
    return url.count('@')
#Sub-directory count.
def countSubDir(url):
    return url.count('/')

def get_ext(url):
    """Return the filename extension from url, or ''."""

    root, ext = splitext(url)
    return ext
def get_filename(url):
    """Return the filename extension from url, or ''."""

    root, ext = splitext(url)
    return root
