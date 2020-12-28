from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os
import sys
import time
print("")
print("")


class FileHandler():

    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode

    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        return self._file


    def __exit__(self, exc_type,exc_value, exc_traceback):
        self._file.close()

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
        topic.append(label.text.replace('/',''))
    counter += 1


#---------SECOND PARSE OF WORDS------------
a = input("Is it alright if we create a few files showing the databank of words for this? If you think you already have it, please input 0. Otherwise, input anything")

if a == "0":
    print("Alright, shutting program...")
    sys.exit()
os.chdir(str(os.getcwd()) + "/Hangman/DataBase")
print("Making files in " + str(os.getcwd()))

counter = 0

for i in topic:
    with FileHandler(i + ".txt", 'w+') as file1:
        website = "https://www.enchantedlearning.com" + links[counter]
        print(website)
        uClient = uReq(my_url)
        page_html =  uClient.read()
        uClient.close()
        page=soup(page_html, "html.parser")
        for word in page.find_all("div",  {"class": "wordlist-item"}):
            file1.write(word.text)
            file1.write("\n")
            print("Hallo")
    counter += 1