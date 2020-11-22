
import requests
from bs4 import BeautifulSoup
import urllib.request
import os
url = input('please get your chapiter manga frome https://3asq.org/ : ')
page = requests.get(url)
print('downloading manga chapiter ...')
soup = BeautifulSoup(page.content ,"html.parser")
title = soup.find("head").find("title").text
pagee =  soup.find_all("img", {"class":"wp-manga-chapter-img"})
dirname = input('please entre path to save your manga :')
for i in pagee:
  urllib.request.urlretrieve(i['src'],dirname + '/'+ i['id']+'.jpg')

print('downloaded manga')
