
import requests
from bs4 import BeautifulSoup
import urllib.request
import os
url = input('please get your chapiter manga from https://3asq.org/ : ')
dirname = input('please entre path to save your manga :')
print('downloading manga chapiter ...')
page = requests.get(url)
soup = BeautifulSoup(page.content ,"html.parser")
title = soup.find("head").find("title").text
pagee =  soup.find_all("img", {"class":"wp-manga-chapter-img"})
for i in pagee:
  urllib.request.urlretrieve(i['src'],dirname + '/'+ i['id']+'.jpg')

print('downloaded manga')
