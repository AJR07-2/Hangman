import random
import os

def generateword(previousword):
    chosen = ""
    with open("words.txt") as topic:
        chosen = random.choice(list(topic))
    
    chosen = chosen.replace("\n", "")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/Database")

    with open(chosen) as word:
        wordchosen = random.choice(list(word))

    wordchosen = wordchosen.replace("\n", "")
    return wordchosen



def checkwin(word):
    if('_' not in word):
        return True
    else:
        return False

def move(word, charguessed):
    print(f"This is the current word: {word}")
    print()





