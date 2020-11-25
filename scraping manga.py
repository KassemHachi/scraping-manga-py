
import requests
from bs4 import BeautifulSoup
import urllib.request
import os
url = input('please get your chapiter manga from https://3asq.org/ : ')
dirname = input('please entre path to save your manga : ')
print('downloading manga chapiter ...')
url = url.replace('/?style=list' , '')
url = url + '/?style=list'
print(url)
page = requests.get(url)
soup = BeautifulSoup(page.content ,"html.parser")
title = soup.find("head").find("title").text
pagee =  soup.find_all("img", {"class":"wp-manga-chapter-img"})
for i in pagee:
  urllib.request.urlretrieve(i['src'], os.path.normpath(dirname + '/'+ i['id']+'.jpg') )
  print(i['id'] + ' is downloaded  ' + '['+ str(pagee.index(i) + 1) + '/' + str(len(pagee))  + ']')
print('downloaded manga')
