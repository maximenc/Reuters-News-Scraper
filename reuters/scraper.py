
from datetime import datetime
from bs4 import BeautifulSoup
from . import article
import requests
import time
import re

def getarticle(link, proxy):

    ctt = requests.get(link, proxies=proxy)
    pageHTML = BeautifulSoup(ctt.content, 'html.parser')

    txt_ = pageHTML.find(class_="StandardArticleBody_body")

    try:
        text = txt_.get_text()
        text = re.sub(r' +', ' ', text)
        text = text.replace('\n', ' ')
    except AttributeError:      #CSS class_ unknown or no text
        text = ""
    
    return text

def scrape(url, proxy):

    list_articles = []
    ctt = requests.get(url, proxies=proxy)
    pageHTML = BeautifulSoup(ctt.content, 'html.parser')

    topStory = pageHTML.find(class_="topStory") 
    # html for top story is different 
    try:
        artcl = article.Article(topStory)
        artcl.text = getarticle(artcl.link, proxy)
        list_articles.append(artcl) 
    except AttributeError:  # except topstory not found
        pass 
    
    features = pageHTML.find_all(class_="feature") 
   
    #find all articles
    for feature in features:
        artcl = article.Article(feature)
        artcl.text = getarticle(artcl.link, proxy)        
        list_articles.append(artcl)
    
    return list_articles
