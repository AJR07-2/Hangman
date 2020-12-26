import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#--------FIRST PARSE OF LINKS----------
my_url = "https://www.enchantedlearning.com/wordlist"
uClient = uReq(my_url)
page_html =  uClient.read()
uClient.close()

page=soup(page_html, "html.parser")

table = page.select("body > p:nth-child(13) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1)")
tables = page.find_all("td")

counter = 12
links = []
topic = []

while counter <= 15:
    container = tables[counter].find_all("a")
    for label in container:
        links.append(label.get('href'))
        topic.append(label.text)
    counter += 1



