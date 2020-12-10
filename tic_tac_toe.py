import random
import copy

def move(x, booly):
    board[x] = booly
    print(x)
    available_moves.pop(available_moves.index(x))

def display_board():
    for i in range(3):
        string = ""
        for j in range(3):
            if board[str(3 * i + j + 1)] == True:
                string += "O "
            elif board[str(3 * i + j + 1)] == False:
                string += "X "
            elif board[str(3 * i + j + 1)] == None:
                string += str(3 * i + j + 1) + " "
        print(string)

def check_score():
    abool = True
    for i in range(8):
        if board[winning_lines[i][0]] == True and board[winning_lines[i][1]] == True and board[winning_lines[i][2]] == True:
            print("Computer won!")
            abool = False
            return True
        elif board[winning_lines[i][0]] == False and board[winning_lines[i][1]] == False and board[winning_lines[i][2]] == False:
            print("You won!")
            abool = False
            return True
    if abool == True:
        bbool = True
        for i in range(9):
            if board[str(i + 1)] == None:
                bbool = False
        if bbool == True:
            print("Draw!")
            return True
    
def check_win():
    for i in range(8):
        if board[winning_lines[i][0]] == True and board[winning_lines[i][1]] == True and board[winning_lines[i][2]] == None:
            return winning_lines[i][2]
        elif board[winning_lines[i][0]] == True and board[winning_lines[i][2]] == True and board[winning_lines[i][1]] == None:
            return winning_lines[i][1]
        elif board[winning_lines[i][1]] == True and board[winning_lines[i][2]] == True and board[winning_lines[i][0]] == None:
            return winning_lines[i][0]

def check_threat():
    for i in range(8):
        if board[winning_lines[i][0]] == False and board[winning_lines[i][1]] == False and board[winning_lines[i][2]] == None:
            return winning_lines[i][2]
        elif board[winning_lines[i][0]] == False and board[winning_lines[i][2]] == False and board[winning_lines[i][1]] == None:
            return winning_lines[i][1]
        elif board[winning_lines[i][1]] == False and board[winning_lines[i][2]] == False and board[winning_lines[i][0]] == None:
            return winning_lines[i][0]

def check_double_attack():
    for a in available_moves:
        pseudo_board = copy.deepcopy(board)
        pseudo_board[a] = True
        counter = 0
        for i in range(8):
            if pseudo_board[winning_lines[i][0]] == True and pseudo_board[winning_lines[i][1]] == True and pseudo_board[winning_lines[i][2]] == None:
                counter += 1
            elif pseudo_board[winning_lines[i][0]] == True and pseudo_board[winning_lines[i][2]] == True and pseudo_board[winning_lines[i][1]] == None:
                counter += 1
            elif pseudo_board[winning_lines[i][1]] == True and pseudo_board[winning_lines[i][2]] == True and pseudo_board[winning_lines[i][0]] == None:
                counter += 1
        if counter >= 2:
            return a

winning_lines = [["1","2","3"],
                 ["4","5","6"],
                 ["7","8","9"],
                 ["1","4","7"],
                 ["2","5","8"],
                 ["3","6","9"],
                 ["1","5","9"],
                 ["3","5","7"]]

available_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
board = {"1": None, "2": None, "3": None, "4": None, "5": None, "6": None, "7": None, "8": None, "9": None}

choice = int(input("Do you want to go first or second? (1 for first and 2 for second): "))
if choice == 2:
    move("5", True)
booly = True
counter = 0
while True:
    display_board()
    selection = input("Enter your choice: ")
    move(selection, False)
    if check_score() == True:
        break
    else:
        if check_win() != None:
            x = check_win()
            move(x, True)
            check_score()
            break
        else:
            if check_threat() != None:
                x = check_threat()
                move(x, True)
            else:
                if check_double_attack() != None:
                    x = check_double_attack()
                    move(x, True)
                else:
                    if choice == 1 and int(selection) % 2 == 0 and counter == 0:
                        x = "5"
                        move(x, True)
                    else:
                        list1 = ["1", "3", "5", "7", "9"]
                        while True:
                            x = random.choice(list1)
                            if x in available_moves:
                                break
                            else:
                                list1.pop(list1.index(x))
                        move(x, True)
    counter += 1
