from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os
import sys
import time
import Functions
print("")
starttime = time.time()

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
        topic.append(label.text.replace('/','').replace("\"", ""))
    counter += 1

#---------SECOND PARSE OF WORDS------------
numberofwords = 0
hallo = input("""Do you have a folder named 'Database' with files inside already? 
If yes, input 1(safer option if this is ur first time running this), if not, input anything else
WARNING: IF THERE IS NO FILES REQUIRED, it might crash!""")

if hallo == "1":
    a = input("""Is it alright if we create a few files showing the databank of words for this? 
WARNING: This takes > 3.35 minutes, depending on internet speed and CPU
If you think you do not have it (checking system to see if u already have it or no coming up), please input 1. Otherwise, input anything. """)

    if a == "1":
        while True:
            try:
                os.chdir(str(os.getcwd()) + "/DataBase")
                break
            except:
                print("U do not have a Database, creating it now...")
                try:
                    directory = "DataBase"
                    parent_dir = os.getcwd()
                    path = os.path.join(parent_dir, directory) 
                    os.mkdir(path) 
                    os.chdir(str(os.getcwd()) + "/DataBase")
                    break
                except:
                    print("Failed to make database, please report error to github")

                
        print("Making files in " + str(os.getcwd()) + " ")

        counter1 = 0

        for i in topic:
            with open(i, 'w+') as file1:
                website = "https://www.enchantedlearning.com" + links[counter1]
                uClient = uReq(website)
                page_html =  uClient.read()
                uClient.close()
                page=soup(page_html, "html.parser")
                for word in page.find_all("div",  {"class": "wordlist-item"}):
                    file1.write(word.text)
                    file1.write("\n")
                    numberofwords += 1
            counter1 += 1
            print(f"Made file with topic {topic[counter1-1]}")

        endtime = time.time()
        totaltime = str(abs(round(starttime - endtime,5)/60))
        print(f"It took {totaltime} minutes to run the program! A total of {numberofwords} words has been added to the database")
        os.chdir("..")