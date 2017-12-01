#Helper class for web parsing using beautiful soup library
import urllib.request
from bs4 import BeautifulSoup




#sample url
#https://www.nytimes.com/2017/11/30/theater/review-in-sleep-a-wakeful-woman-faces-long-surreal-nights.html

class WebParser():
    #global fields & constructor

    url = ""

    def __init__(self):
        #self.url = "https://www.nytimes.com/2017/11/30/theater/review-in-sleep-a-wakeful-woman-faces-long-surreal-nights.html"
        self.url="https://www.nytimes.com/2017/11/30/us/politics/state-department-tillerson-pompeo-trump.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news"

    ###

    #fuctions go here.
    def open_url(self):
        page = urllib.request.urlopen(self.url).read()

        soup = BeautifulSoup(page,'html.parser')
        #print(soup.prettify)
        article_body = soup.find_all('p','story-body-text') #will extract the text based on the hardcoded class name
        for content in article_body:
            print(content.getText())
