'''
Created on 17/02/2019

@author: dinis
'''
from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.gutenberg.org/files/135/135-h/135-h.htm")

content= html.content
cenas=html.encoding

html = html.text
soup = BeautifulSoup(html,"html.parser")
#print (content)


#===============================================================================
# with open("texto.txt","w", encoding="utf-8") as f:
#     f.write(html)
#===============================================================================
with open("data.txt","w", encoding="utf-8") as fd:
    fd.write(soup.get_text())
print (soup.encoding)

sad = 0
list_of_words = html.split(" ")
#print (list_of_words)
for word in list_of_words:
    if word == "sad":
        sad +=1

print (sad)