#Helper class for web parsing using beautiful soup library
import urllib.request
from bs4 import BeautifulSoup

# 10 test urls
# 1)  https://www.nytimes.com/aponline/2017/11/30/sports/ncaabasketball/ap-bkc-t25-notre-dame-michigan-st.html
# 2)  https://www.nytimes.com/aponline/2017/11/30/sports/ncaabasketball/ap-bkw-t25-ohio-state-duke.html
# 3)  https://www.nytimes.com/aponline/2017/11/30/sports/ncaabasketball/ap-bkw-t25-central-arkansas-tennessee.html
# 4)  https://www.nytimes.com/aponline/2017/11/30/sports/ncaabasketball/ap-bkc-t25-texas-tech-seton-hall.html
# 5)  https://www.nytimes.com/aponline/2017/11/30/sports/ncaabasketball/ap-bkw-t25-western-carolina-south-carolina.html
# 6)  https://www.nytimes.com/aponline/2017/11/30/sports/ap-car-nascar-most-popular.html
# 7)  https://www.nytimes.com/2017/11/30/us/politics/trump-russia-senate-intel.html
# 8)  https://www.nytimes.com/aponline/2017/11/30/sports/ap-car-nascar-france-award.html
# 9)  https://www.nytimes.com/2017/11/30/sports/ohtani-bidding-baseball-21-days.html
# 10)  https://www.nytimes.com/aponline/2017/11/30/us/ap-us-kansas-shooting-lawsuit.html



#sample url
#https://www.nytimes.com/2017/11/30/theater/review-in-sleep-a-wakeful-woman-faces-long-surreal-nights.html

class WebParser():
    #global fields & constructor

    url = ""

    def __init__(self):
        #self.url = "https://www.nytimes.com/2017/11/30/theater/review-in-sleep-a-wakeful-woman-faces-long-surreal-nights.html" #test url 1
        self.url="https://www.nytimes.com/2017/11/30/us/politics/state-department-tillerson-pompeo-trump.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news" #test url 2

    ###

    #fuctions go here.
    def extract_body(self):
        page = urllib.request.urlopen(self.url).read()

        soup = BeautifulSoup(page,'html.parser')
        #print(soup.prettify)
        article_body = soup.find_all('p','story-body-text') #will extract the text based on the hardcoded class name
        
        final_body = ""#the article body that will be returned.
        final_body = final_body+ soup.title.getText()#append the title to the article
        
        print(soup.title.getText())
        for content in article_body:
            #print(content.getText())
            final_body = final_body + content.getText()

        return final_body


