import os
from bs4 import BeautifulSoup
from requests_html import HTMLSession
session = HTMLSession()
import webbrowser
from selenium import webdriver



useinp = input("Enter Search Term: ")
useinp = useinp.replace(' ','+')
useinp = useinp.lower()
netlink = "https://music.youtube.com/search?q="+str(useinp)

from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-gpu")

chrome_options.add_argument("--sheadless")

driver = webdriver.Chrome(options=chrome_options)


driver.get(netlink)

print(driver.page_source.encode("utf-8"))

driver.quit()
