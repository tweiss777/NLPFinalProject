import json
import urllib.request
import sys
import time

#Testing nyt api
#API key for nyt article search = c0e62e93aa63482185d40750586dfbab
#google news api key = daeaeab2284c44b093f841c7a9ca10ab
#WARNING: NYTAPI IS LIMITED TO 1000 CALLS A DAY!
class NewsApi():
    
    def google_news_extract(self,query):
        urls = []
        try:#exception handling incase user does not input an integer
            print("\nwill retrun the first 10 urls if left blank\n")
            pages = int(input("Enter the number of pages to return -> "))
        except ValueError:
            pages = 0
        #sample url:https://newsapi.org/v2/everything?q=bitcoin&apiKey=daeaeab2284c44b093f841c7a9ca10ab
        base_url = "https://newsapi.org/v2/everything?"
        
        for page in range(0,pages+1):
            params = {'q': query,'apiKey':'daeaeab2284c44b093f841c7a9ca10ab','page':pages}
            url = base_url + urllib.parse.urlencode(params)
            api_call = urllib.request.urlopen(url).read()
            decoded_data = api_call.decode('utf-8')
            data = json.loads(decoded_data)

            for article in data['articles']:
                print(article['url'])
                urls.append(article['url'])
        
        return urls
    #being replaced by google
    def process_nyt(self,query): #url is encoded using urlencode
    #to return a list of urls
        pages = 0
        
        url_list = [] #holds the lsit of urls returned by the api
        try:#exception handling incase user does not input an integer
            print("\nwill retrun the first 10 urls if left blank\n")
            pages = int(input("Enter the number of pages to return -> "))
        except ValueError:
            pages = 0
        
        url_count = 0 #keep track of the urls shown
        for i in range(0,pages+1):
            base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"
            params = {'api-key': 'c0e62e93aa63482185d40750586dfbab', '?q': query, '?page':i}
        
            #open the url and call the api
            url = base_url + urllib.parse.urlencode(params)
            api_call = urllib.request.urlopen(url).read()
            decoded_data = api_call.decode('utf-8')
            
            
            #json data gets stored here
            data = json.loads(decoded_data)
            
            for doc in data['response']['docs']:
                url_count+=1
                if(doc['web_url'] not in url_list):
                    url_list.append(doc['web_url'])
            #time.sleep(5)
        return url_list #returns the url list.
        
