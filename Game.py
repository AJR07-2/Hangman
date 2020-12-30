import random
import os
def generateword(previousword):
    topic = open("words.txt", "w+")
    randomtopic = random.randint(1, 169)
    counter = 1
    for word in topic:
        if counter == randomtopic:
            chosen = word
            break
        counter += 1
    topic.close()
    os.chdir(str(os.mkdir())+ "/Database")
    worddict = open(chosen, "w+")
    randomword = random.randint(1, file_len(chosen))
    counter = 1
    for word in worddict:
        if counter == randomword:
            chosen = word
            break
        counter += 1
    worddict.close()
    return chosen


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1