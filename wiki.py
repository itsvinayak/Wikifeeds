# import requests
# from bs4 import BeautifulSoup as bs
#
#
# responce = requests.get('https://en.wikipedia.org/wiki/Special:Random')
#
# if responce.ok:
#     soup = bs(responce.text,'lxml')
#     title=soup.find('h1', class_='firstHeading').string
#     img=soup.find('img')['src']
#     text=soup.p.string
#
#     data={
#           'title':title,
#           'img':img,
#           'text':text,
#     }
#
#     print(data)


import wikipedia

source = wikipedia.page(wikipedia.random(pages=1))

title = source.title
img = source.images[0]
url = source.url
text = source.content

data={
           'title':title,
           'img':img,
           'text':text,
           'url':url,
     }

print(data)
