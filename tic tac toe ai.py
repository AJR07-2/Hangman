import time
# Instructions for player
print("This tic tac toe AI Machine has been created by Ang Jun Ray. 23 Nov 2020")
print("*********TO REQUEST MORE FEATURES/RSPORT A BUG, PLEASE LEAVE A NOTE ON GITHUB. *******")
print("To play with the program, please input the place you would want to place your X or 0")
print("It is defined by (row character)(column number)")
time.sleep(5)
#inputs
while True:
    a = input("Would you like to go first? (Yes/No)")
    if a == "Yes" or a == "No":
        break
    else:
        print("Capitalization matters, please input exactly Yes or No")
if a  == "Yes":
