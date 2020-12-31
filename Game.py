import random
import os

class FileHandler():

    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode

    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        return self._file


    def __exit__(self, exc_type,exc_value, exc_traceback):
        self._file.close()

def generateword(previousword):
    chosen = ""
    topic = open("words.txt", "r")
    randomtopic = random.randint(1, 169)
    counter = 1
    for word in topic:
        if counter == randomtopic:
            chosen = word
            break
        counter += 1
    topic.close()
    chosen = chosen.replace("\n", "")
    os.chdir(str(os.getcwd()) + "/Database")
    worddict = open(chosen, "w+")
    a = file_len(chosen)
    randomword = random.randint(1, a)
    counter = 1
    for word in worddict:
        if counter == randomword:
            chosen = word
            break
        counter += 1
    worddict.close()
    return chosen


def file_len(fname):
    counter = 0
    with FileHandler(fname, "r") as f:
        for i in f:
            counter += 1
    print(counter)
    return counter