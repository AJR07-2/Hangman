import random
import os
import Hangman_py

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

def move(word, guessedletters):
    print(f"This is the current word: {word}")
    
    while True:
        chaguessed = input("Guess a letter:")
        if len(chaguessed) != 1:
            Hangman_py.error(chaguessed, "only a single character is allowed")
        elif chaguessed in guessedletters:
            Hangman_py.error(chaguessed, f"letter has beenguessed before, here is your current list of guessed letters: {guessedletters}")
