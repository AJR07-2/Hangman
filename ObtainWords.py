from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os
import sys
import time
print("")
print("")
starttime = time.time()

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

file2 = open("topics.txt", "w+")

while counter <= 15:
    container = tables[counter].find_all("a")
    for label in container:
        links.append(label.get('href'))
        topic1 = label.text.replace('/','')
        topic.append(topic1.replace("\"", ""))
        file2.write(topic1.replace("\"", ""))
        file2.write("\n")
    counter += 1
file2.close

#---------SECOND PARSE OF WORDS------------

hallo = input("""Do you have a folder named 'Database' with files inside already? 
If yes, input 1(safer option if this is ur first time running this), if not, input anything else
WARNING: IF THERE IS NO FILES REQUIRED, it might crash!""")

if hallo != "1":
    sys.exit

a = input("""Is it alright if we create a few files showing the databank of words for this? 
WARNING: This takes > 3.35 minutes, depending on internet speed and CPU
If you think you already have it (checking system to see if u already have it or no coming up), please input 0. Otherwise, input anything. """)

if a == "0":
    print("Alright, shutting program...")
    sys.exit()
os.chdir(str(os.getcwd()) + "/Hangman/DataBase")
print("Making files in " + str(os.getcwd()) + " ")

counter1 = 0

for i in topic:
    with FileHandler(i, 'w+') as file1:
        website = "https://www.enchantedlearning.com" + links[counter1]
        uClient = uReq(website)
        page_html =  uClient.read()
        uClient.close()
        page=soup(page_html, "html.parser")
        for word in page.find_all("div",  {"class": "wordlist-item"}):
            file1.write(word.text)
            file1.write("\n")
    counter1 += 1
    print("Made file with topic " + topic[counter1-1])

endtime = time.time()

print("It took " + str(abs(round(starttime - endtime,5)/60)) + " minutes to run the program!")