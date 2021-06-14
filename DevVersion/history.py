import os
from bs4 import BeautifulSoup
from requests_html import HTMLSession
session = HTMLSession()

histsource = "https://assassinscreed.fandom.com/wiki/Database"
histsoup = (histsource,'lxml')

links = histsoup.find_all('href')
print(links)
