
#--------------------
#importing
#--------------------
import time
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import os
import Game
#--------------------
#introduction
#--------------------
intro = """
Hello there, this is a Hangman Game made by AJR, Dec 23 2020
More improvements will be made in the future, feel free to open an issue if u have any suggestions or there is any bugs!
Thanks and enjoy! :D

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

--------FUTURE IMPROVEMENTS---------
1. App
2. more words
3. multiplayer
"""

print(intro)
time.sleep(1)

os.chdir(str(os.getcwd()) + "/Hangman")
exec(open('ObtainWords.py').read())
#--------------------
#functions
#--------------------

def error(input, requirements):
  print(f"Ur input: {input} is Invalid. This is because: {requirements} ")

#gathering the list of topics for the game
myList = []
words = open("words.txt", "r")
for topic in words:
  myList.append(topic.rstrip("\n"))
words.close()

#--------------------
#topic choice
#--------------------

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

ganeratedWord = Game.generateword("", topic)

word = list(ganeratedWord)
guessedletters = 0 #incldues duplicates
guessedalph = []
lives = 5

while guessedletters < len(ganeratedWord):
  print("You have 5 lives, each incorrect guess is 1 live subtracted")
  result = Game.move(word, guessedalph, lives)
  guessedalph.append(result[1])
  guessedletters += int(result[0])
  lives = int(result[2])
  




#--------------------
#end of program
#--------------------
endtime = time.time()
totaltime = startime - endtime
totaltime = str(abs(round(totaltime,5)))
print(f"You took {totaltime} seconds to complete the Hangman word!")