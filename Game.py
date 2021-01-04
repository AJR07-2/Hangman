import random
import os
import pictures

def error(input, requirements):
  print(f"Ur input: {input} is Invalid. This is because: {requirements} ")

def generateword(previousword,chosen):
    chosen = chosen.replace("\n", "")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/Database")

    with open(chosen) as word:
        wordchosen = random.choice(list(word))

    wordchosen = wordchosen.replace("\n", "")
    return wordchosen


def separationline():
    print("---------------------------------------------------------------------------------")

    pictures.Pictures.

def enumChecker(lives):
    print("Current live counts:")
    if lives-1 == 6:
        print(pictures.Pictures.six)
    elif lives-1 == 5:
        print(pictures.Pictures.five)
    elif lives-1 == 4:
        print(pictures.Pictures.four)
    elif lives-1 == 3:
        print(pictures.Pictures.three)
    elif lives-1 == 2:
        print(pictures.Pictures.two)
    elif lives-1 == 1:
        print(pictures.Pictures.one)
    elif lives-1 == 0:
        print(pictures.Pictures.zero)

def checkwin(word):
    if('_' not in word):
        return True
    else:
        return False

def printword(word):
    printtext = ""
    for i in word:
        printtext += i
    print(f"This is the current word {printtext}")

def move(word, guessedletters, lives, guessedword):
    printword(guessedword)
    detials = [] #1. amount of letters guessed(non-unique), 2. letter guessed, 3, lives
    while True:
        chaguessed = input("Guess a letter:")
        if len(chaguessed) != 1:
            error(chaguessed, "only a single character is allowed")
        elif chaguessed in guessedletters:
            error(chaguessed, f"letter has been guessed before, here is your current list of guessed letters: {guessedletters}")
        elif chaguessed.isalpha == False:
            error(chaguessed, "Hmm, it seems like ur input isn't an alphabet")
        else:
            if chaguessed in word:
                ocurrences = str(word.count(chaguessed))
                detials.append(ocurrences)
                detials.append(chaguessed)
                print(f"{chaguessed} is in the word! There were {ocurrences} '{chaguessed}'s in the word!")
                detials.append(str(lives))
            
            else:
                detials.append("0")
                detials.append(chaguessed)
                detials.append(str(lives-1))
                print(f"{chaguessed} is not in the word :(. 1 life has been lost, u currently have {lives-1} lives!")
            enumChecker(lives)


            break
    separationline()
    return detials