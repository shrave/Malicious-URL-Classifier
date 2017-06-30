
nf=-1
def url_length(url):
    return len(url)
def ratio_special_chars(url):
count=0
    for i in url:
        if i not i.isalnum():
                count=count+1
    return float(count/len(url))

def Tokenise(url):

        if url=='':
            return [0,0,0]
        token_word=re.split('\W+',url)
        #print token_word
        return token_word
'''        no_ele=sum_len=largest=0
        for ele in token_word:
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
    
