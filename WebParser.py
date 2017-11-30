#Helper class for web parsing using beautiful soup library
import urllib.request
from bs4 import BeautifulSoup




#sample url
#https://www.nytimes.com/2017/11/30/theater/review-in-sleep-a-wakeful-woman-faces-long-surreal-nights.html

class WebParser():
    #global fields & constructor

    url = ""

    def __init__(self):
        self.url = "https://www.nytimes.com/2017/11/30/theater/review-in-sleep-a-wakeful-woman-faces-long-surreal-nights.html"

    ###

    #fuctions go here.
    def open_url(self):
        page = urllib.request.urlopen(self.url).read()

        soup = BeautifulSoup(page,'html.parser')
        print(soup.prettify)
