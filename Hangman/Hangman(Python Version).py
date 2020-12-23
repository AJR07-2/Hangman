print("Hallo")
#gathering the list of topics for the game
myList = []
words = open("/Users/angjunray/Desktop/Coding/General/Projects/Hangman/words.txt", "r")
for topic in words:
  myList.append(topic)

#topic choice
topic = input("What topic do you want to choose? Type ? for list of topics!")
if topic == "?":
  print("----------LIST OF TOPICS AVALIABLE------------")
  for word in myList:
    print(word)
  
  print("------------------END OF LIST-----------------")
