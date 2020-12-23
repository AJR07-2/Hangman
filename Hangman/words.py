import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

my_url = "https://www.enchantedlearning.com/wordlist/"

#Opening up connections
uClient = uReq(my_url)

#grabbing the page
page_html =  uClient.read()
uClient.close()
print(page_html)

#html parsing
page_soup=soup(page_html, "html.parser")

print(page_soup.h1)
print("Hallo")