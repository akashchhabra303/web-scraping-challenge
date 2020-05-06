# converting your Jupyter notebook into a Python script called
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import requests
# import pymongo
import numpy as np
import pandas as pd
# from pprint import pprint

print('hello world')

mars_dict ={}

def scrape():
    file_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    print(file_url)
    page=requests.get(file_url)
    print(page.status_code)
    soup=bs(page.content,'html.parser')
    print(soup.prettify())

    title = soup.find_all('div', class_="content_title")
    news_title = title[0].text
    mars_dict['news_title'] = news_title

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
    news_p = paragraph_list[0]
    mars_dict['news_p'] = news_p

    file_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    page=requests.get(file_url)
    soup=bs(page.content,'html.parser')
    images =soup.find_all('div',class_='img')
    
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
    # print(img_pics)
    mars_dict['image_pics']=img_pics


    file_url = 'https://twitter.com/marswxreport?lang=en'
    page=requests.get(file_url)
    print(page.status_code)
    # print(page.content)
    soup=bs(page.content,'html.parser')
    # print(soup.prettify())
    tweets = soup.find_all('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    tweets = tweets[0].text
    mars_dict['tweets']=tweets
   

    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    page=requests.get(hemispheres_url)
    
    soup=bs(page.content,'html.parser')
    hemispheres_image = soup.find_all('div',class_= 'item')
    
    hemispheres_img_list = []
    for result in hemispheres_image:
    # Error handling
        try:
            link = result.a['href']        
            hemispheres_img_list.append(('https://astrogeology.usgs.gov') + (link))
            
        except AttributeError as e:
            print(e)
    mars_dict["hemispheres"] = hemispheres_img_list
    # scrape_dict={'hem':hemispheres_img_list,'tweet':tweets_list,'img':img_pics,'paragraph':paragraph_list,'title':title_list}

    url = 'http://space-facts.com/mars/'
    marsfacts = pd.read_html(url)
    #marsfacts
    
    # Using .rename(columns={}) in order to rename columns
    marsfacts_df = marsfacts[0]
    renamed_marsfacts_df = marsfacts_df.rename(columns={0:"Facts", 1:"Value"})
    # renamed_marsfacts_df1 = renamed_marsfacts_df.set_index('Facts')
        
    #Convert df to html table string
    marsfacts_html=renamed_marsfacts_df.to_html()
    print('hello')
    mars_dict["Facts"] = marsfacts_html
     
    return mars_dict
   
# scrape()