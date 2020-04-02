# converting your Jupyter notebook into a Python script called
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import requests
import pymongo
import numpy as np
from pprint import pprint

print('hello world')

def scrape():
    file_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    print(file_url)
    page=requests.get(file_url)
    print(page.status_code)
    soup=bs(page.content,'html.parser')
    print(soup.prettify())

    title = soup.find_all('div', class_="content_title")
    print(title)
    title_list = []
    for result in title:
        try:
            title = result.find('a').text
            print(title)
            title_list.append(title)
        except AttributeError as e:
            print(e)
    print(len(title_list))
    paragraph = soup.find_all('div',class_='rollover_description')
    print(paragraph)

    paragraph_list=[]
    for result in paragraph:
        try:
            text= result.text
            paragraph_list.append(text)
            print(text)
        except AttributeError as e:
            print(e)
        print(len(paragraph_list))

    file_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


    page=requests.get(file_url)
    print(page.status_code)
    # print(page.content)

    soup=bs(page.content,'html.parser')
    print(soup.prettify())

    images =soup.find_all('div',class_='img')
    print(images)

    img_pics=[]
    for result in images:
    # Error handling
        try:
            img = result.img
            link = result.img['src']
            img_pics= ((file_url) + (link))
#         img_link = (file_url) + (link)
#         print(img_link)
        except AttributeError as e:
            print(e)
    print(len(img_pics))


    file_url = 'https://twitter.com/marswxreport?lang=en'


    page=requests.get(file_url)
    print(page.status_code)
    # print(page.content)

    soup=bs(page.content,'html.parser')
    print(soup.prettify())

    tweets = soup.find_all('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    print(tweets)

    tweets_list=[]

    for result in tweets:
    # Error handling
        try:
            text = result.get_text()
            
            tweets_list.append(str)
            print(tweets)
        except AttributeError as e:
            print(e)
    print(len(tweets_list))

    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


    page=requests.get(hemispheres_url)
    print(page.status_code)
    # print(page.content)

    soup=bs(page.content,'html.parser')
    print(soup.prettify())    

    hemispheres_image = soup.find_all('div',class_= 'item')
    print(len(hemispheres_image))

    hemispheres_img_list = []
    for result in hemispheres_image:
    # Error handling
        try:
            link = result.a['href']
    #         print(hemispheres_url)
    #         print(link)
            hemispheres_img_list= (('https://astrogeology.usgs.gov') + (link))
            print(hemispheres_img_list)
        except AttributeError as e:
            print(e)

    scrape_dict={'hem':hemispheres_img_list,'tweet':tweets_list,'img':img_pics,'paragraph':paragraph_list,'title':title_list}

    return scrape_dict
scrape()