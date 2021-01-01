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

def move(word, guessedletters, lives):
    print(f"This is the current word: {word}")
    detials = [] #1. amount of letters guessed(non-unique), 2. letter guessed, 3, lives
    while True:
        chaguessed = input("Guess a letter:")
        if len(chaguessed) != 1:
            Hangman_py.error(chaguessed, "only a single character is allowed")
        elif chaguessed in guessedletters:
            Hangman_py.error(chaguessed, f"letter has beenguessed before, here is your current list of guessed letters: {guessedletters}")
        elif chaguessed.isalpha == False:
            Hangman_py.error(chaguessed, "Hmm, it seems like ur input isn't an alphabet")
        else:
            if chaguessed in word:
                ocurrences = str(list.count(chaguessed))
                detials.append(ocurrences)
                detials.append(chaguessed)
                print(f"{chaguessed} is in the word! There were {ocurrences} '{chaguessed}'s in the word!")
                detials.append(str(lives))
            
            else:
                detials.append("0")
                detials.append(chaguessed)
                detials.append(str(lives-1))
                print(f"{chaguessed} is not in the word :(. 1 life has been lost, u currently have {lives-1} lives!")
            break
    return detials