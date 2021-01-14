# --------------------
# importing
# --------------------
import time
import Functions
import bs4
from urllib.request import urlopen as uReq
import os
from bs4 import BeautifulSoup as soup

# --------------------
# introduction
# --------------------
intro = r"""
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
Functions.separationLine()
Functions.separationLine()

print(intro)
time.sleep(4)

Functions.separationLine()

import ObtainWords

Functions.separationLine()
Functions.separationLine()


# gathering the list of topics for the game
myList = []
words = open("words.txt", "r")
for topic in words:
    myList.append(topic.rstrip("\n"))
words.close()

# --------------------
# topic choice
# --------------------

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
        Functions.error(
            topic,
            "Input must be in the list of topics. Input ? for list! (Please check if ur caps differs. It matters!)",
        )

Functions.separationLine()
Functions.separationLine()
Functions.separationLine()

# time
startime = time.time()

# Program itself
generatedWord = Functions.generateWord("", topic)

shownToUser = []
for i in generatedWord:
    shownToUser.append("_")
word = list(generatedWord)
guessedletters = 0  # incldues duplicates
guessedAlph = []
lives = 5
print("You have 6 lives, each incorrect guess is 1 live subtracted")

Functions.enumChecker(7)

while guessedletters < len(generatedWord):
    result = Functions.move(word, guessedAlph, lives, shownToUser)
    guessedAlph.append(result[1])
    guessedletters += int(result[0])
    lives = int(result[2])

    counter = 0
    for i in generatedWord:
        if result[1] == i:
            shownToUser[counter] = result[1]
        counter += 1

    if lives == 0:
        print(
            f"Oh no, u have lost all your lives :( THe word was {generatedWord}. Try again next time!"
        )
        break
    if "_" not in shownToUser:
        print("You have won! Good job :D")
        break
    time.sleep(2)

Functions.enumChecker(lives + 1)

Functions.separationLine()
Functions.separationLine()


print(
    """The word database is taken from enchantedlearning.com.
Hangman ASCII pictures are taken from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c.
Thanks for playing! More features coming soon!"""
)

Functions.separationLine()

# --------------------
# end of program
# --------------------
endtime = time.time()
totaltime = startime - endtime
totaltime = str(abs(round(totaltime / 60, 2)))
print(f"You took {totaltime} minutes to complete the Hangman word program!")
time.sleep(10)
