
import requests
from bs4 import BeautifulSoup
import urllib.request

page = requests.get("https://3asq.org/manga/dr-stone/163/")
soup = BeautifulSoup(page.content ,"html.parser")

pagee =  soup.find_all("img", {"class":"wp-manga-chapter-img"})
for i in pagee:
  urllib.request.urlretrieve(i['src'],i['id']+'.jpg')

print('downloaded images')
