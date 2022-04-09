import requests
from bs4 import BeautifulSoup as soup
Send get request:
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia&cy=AU'
page = requests.get(URL)
Get Job title:
title = []
for header in bsobj.findAll('h2',{'class':'title'}):
  title.append(header.text.strip())