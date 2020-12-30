import time
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import os

#--------------------
#introduction
#--------------------
intro = """
Hello there, this is a Hangman Game made by AJR, Dec 23 2020
More improvements will be made in the future, feel free to open an issue if u have any suggestions/There is any bugs!
Thanks and enjoy! :D

--------FUTURE IMPROVEMENTS---------
1. App
2. more words
3. multiplayer
"""

print(intro)
time.sleep(5)



os.system('ObtainWords.py')

#--------------------
#functions
#--------------------

def error(input, requirements):
  print("Ur input: " + input + " is Invalid. Please input acccording to the requirements of(" + requirements + ") instead.")

#gathering the list of topics for the game
myList = []
words = open("/Users/angjunray/Desktop/Coding/General/Projects/Hangman/words.txt", "r")
for topic in words:
  myList.append(topic.rstrip("\n"))

#--------------------
#topic choice
#--------------------

topicfile = open("topics.txt", "w+")


topicfile.close()

while True:
  topic = input("What topic do you want to choose? Type ? for list of topics!")
  if topic == "?":
    print("----------LIST OF TOPICS AVALIABLE------------")
    for word in myList:
      print(word)    
    print("------------------END OF LIST-----------------")
  elif topic in myList:
    break
  else:
    error(topic, "Input must be in the list of topics. input ? for list!")


#time 
startime = time.time()







#check time
endtime = time.time()
totaltime = startime - endtime
print("You took " + str(abs(round(totaltime,5))) + " seconds to complete the Hangman word!")