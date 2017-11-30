import json
import urllib.request

#Testing nyt api
#API key for nyt article search = c0e62e93aa63482185d40750586dfbab

def process_nyt(): #url is hardcoded here
    
    article_urls = [] #holds the list of urls
    api_key = "c0e62e93aa63482185d40750586dfbab"
    query = input("enter a search")
    pages = 0 # page number shows 10 urls. 0 show the first 10 results

    
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key="+api_key+"&?q="+query+"&?page="+str(pages)
    print("url= ",url)
    
    api_call = urllib.request.urlopen(url).read()
    decode = api_call.decode('utf-8')
    load_data = json.loads(decode)

def nyt2(): #url is encoded using urlencode
    query = input("enter a search term")
    pages = 0
    base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"
    params = {'api-key': 'c0e62e93aa63482185d40750586dfbab', '?q': query, '?page': pages}
    
    url = base_url + urllib.parse.urlencode(params)
    api_call = urllib.request.urlopen(url).read()
    decoded_data = api_call.decode('utf-8')
    data = json.loads(decoded_data)
    print(data)
    data[]



    

def main():
    #process_nyt()
    nyt2()
main()
