import requests
from bs4 import BeautifulSoup
import time

page = requests.get("https://manganelo.com/chapter/read_detective_conan_manga_online_free/chapter_1060")
soup = BeautifulSoup(page.content ,"html.parser")

chapiter =  soup.find("div", {"class":"container-chapter-reader"})
mangas = chapiter.find_all('img')
file = open('scrapin-output.html','w') 
file.write("<!DOCTYPE html><html lang='en'> <head> <meta charset='UTF-8'>  <meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Document</title></head><body>")

file.write(str(mangas)) 
file.write("</body></html>")
 
file.close()
print('html created')
# for image in mangas:
#     url = image['src']
#     filename = url.split("/")[-1]
#     req = requests.get(url)

#     with open(filename, 'wb') as f:
#       f.write(req.content)
#     time.sleep(10)
#     # r = requests.get(url)
#     # with open(image['alt'] + ".jpg", 'wb') as f:
#     #     f.write(r.content)
#     #     f.close
#     print (url)
