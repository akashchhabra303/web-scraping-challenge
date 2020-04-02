#         paragraph_list=[]

#     for result in paragraph:
#         # Error handling
#         try:
#             text = result.text
#             paragraph_list.append(text)

#         except AttributeError as e:


#     file_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


#     page=requests.get(file_url)

#     # print(page.content)

#     soup=bs(page.content,'html.parser')


#     images = soup.find_all('div',class_= 'img')


#     img_pics=[]
#     for result in images:
#         # Error handling
#         try:
#             img = result.img
#             link = result.img['src']
#             img_pics= ((file_url) + (link))
#     #         img_link = (file_url) + (link)
#     #         print(img_link)
#         except AttributeError as e:


#     file_url = 'https://twitter.com/marswxreport?lang=en'


#     page=requests.get(file_url)

#     # print(page.content)

#     soup=bs(page.content,'html.parser')


#     tweets = soup.find_all('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')


#     tweets_list=[]

#     for result in tweets:
#         # Error handling
#         try:
#             text = result.get_text()
            
#             tweets_list.append(str)

#         except AttributeError as e:


#     hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


#     page=requests.get(hemispheres_url)

#     # print(page.content)

#     soup=bs(page.content,'html.parser')


#     hemispheres_image = soup.find_all('div',class_= 'item')




#     hemispheres_img_list = []
#     for result in hemispheres_image:
#         # Error handling
#         try:
#             link = result.a['href']
#     #         print(hemispheres_url)
#     #         print(link)
#             hemispheres_img_list= (('https://astrogeology.usgs.gov') + (link))

#         except AttributeError as e:
