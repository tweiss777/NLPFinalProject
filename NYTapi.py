import json
import urllib.request
import sys

#Testing nyt api
#API key for nyt article search = c0e62e93aa63482185d40750586dfbab
#WARNING: API IS LIMITED TO 1000 CALLS A DAY!
class NewYorkTimes():
    

    def process_nyt(self): #url is encoded using urlencode
    #to return a list of urls
        query = input("enter a search term query-> ")
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
                print(str(url_count)+") ",doc['web_url'])
                url_list.append(doc['web_url'])
        return url_list #returns the url list.
        
