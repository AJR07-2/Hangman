#include <bits/stdc++.h>
using namespace std;

// ------------------------------------------------------------------
// DECLARATION OF VARIABLES------------------------------------------
// ------------------------------------------------------------------

string winning_lines[8][3] = {{"1", "2", "3"}, {"4", "5", "6"}, {"7", "8", "9"}, {"1", "4", "7"}, {"2", "5", "8"}, {"3", "6", "9"}, {"1", "5", "9"}, {"3", "5", "7"}};
string available_moves[10] = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
map <string,int> a = {{"1", 0}, {"2", 0}, {"3", 0}, {"4", 0}, {"5", 0}, {"6", 0}, {"7", 0} ,{"8", 0}, {"9", 0}};


// ------------------------------------------------------------------
// INSTRUCTIONS FOR PLAYER-------------------------------------------
// ------------------------------------------------------------------

cout << "This tic tac toe AI Machine has been created by AJR07, Collaborated by YNWAPythoner. 23 Nov 2020" << '\n' << "*********TO REQUEST MORE FEATURES/REPORT A BUG, PLEASE LEAVE A NOTE ON GITHUB. *******" << '\n' << "To play with the program, please input the place you would want to place your X" << '\n';
time.sleep(1)
print("It is defined by (row character)(column number)")
print("This is the board:")
print("1 2 3")
print("4 5 6")
print("7 8 9")
time.sleep(1)
print("The indexes are what you are supposed to enter to select a move later on")
print("The player would be X all the time, whether he moves first or not. (Could be changed in the future)")
time.sleep(5)


# ------------------------------------------------------------------
# FUNCTIONS---------------------------------------------------------
# ------------------------------------------------------------------
def display_board():
    for i in range(3):
        string = ""
        for j in range(3):
            if board[str(3 * i + j + 1)]:
                string += "O "
            elif board[str(3 * i + j + 1)] == False:
                string += "X "
            elif board[str(3 * i + j + 1)] is None:
                string += "_ "
        print(string)


def check_score():
    abool = True
    for i in range(8):
        if board[winning_lines[i][0]] == True and board[winning_lines[i][1]] == True and board[
            winning_lines[i][2]] == True:
            print("Computer won!")
            abool = False
            return True
        elif board[winning_lines[i][0]] == False and board[winning_lines[i][1]] == False and board[
            winning_lines[i][2]] == False:
            print("You won!")
            abool = False
            return True
    if abool:
        bbool = True
        for i in range(9):
            if board[str(i + 1)] is None:
                bbool = False
        if bbool:
            print("Draw!")
            return True


def check_win():
    for i in range(8):
        if board[winning_lines[i][0]] == True and board[winning_lines[i][1]] == True and board[
            winning_lines[i][2]] == None:
            return winning_lines[i][2]
        elif board[winning_lines[i][0]] == True and board[winning_lines[i][2]] == True and board[
            winning_lines[i][1]] == None:
            return winning_lines[i][1]
        elif board[winning_lines[i][1]] == True and board[winning_lines[i][2]] == True and board[
            winning_lines[i][0]] == None:
            return winning_lines[i][0]


def check_double_attack():
    for a in available_moves:
        pseudo_board = copy.deepcopy(board)
        pseudo_board[a] = True
        counter = 0
        for i in range(8):
            if pseudo_board[winning_lines[i][0]] == True and pseudo_board[winning_lines[i][1]] == True and \
                    pseudo_board[winning_lines[i][2]] == None:
                counter += 1
            elif pseudo_board[winning_lines[i][0]] == True and pseudo_board[winning_lines[i][2]] == True and \
                    pseudo_board[winning_lines[i][1]] == None:
                counter += 1
            elif pseudo_board[winning_lines[i][1]] == True and pseudo_board[winning_lines[i][2]] == True and \
                    pseudo_board[winning_lines[i][0]] == None:
                counter += 1
        if counter >= 2:
            return a


def check_threat():
    for i in range(8):
        if board[winning_lines[i][0]] == False and board[winning_lines[i][1]] == False and board[
            winning_lines[i][2]] == None:
            return winning_lines[i][2]
        elif board[winning_lines[i][0]] == False and board[winning_lines[i][2]] == False and board[
            winning_lines[i][1]] == None:
            return winning_lines[i][1]
        elif board[winning_lines[i][1]] == False and board[winning_lines[i][2]] == False and board[
            winning_lines[i][0]] == None:
            return winning_lines[i][0]




# ------------------------------------------------------------------
# INPUTS
# ------------------------------------------------------------------

while True:
    try:
        choice = int(input("Do you want to go first or second? (1 for first and 2 for second): "))
    except:
        print("That input is invalid, please retry")
        continue
    if choice == 1 or choice == 2:
        break
    else:
        print("That input is invalid, please retry")
    time.sleep(2)

if choice == 2:
    board["5"] = True
    print("Computer played: 5")
    available_moves.pop(available_moves.index("5"))
booly = True
while True:
    display_board()
    selection = input("Enter your choice: ")
    x = selection
    board[x] = False
    available_moves.pop(available_moves.index(x))
    if check_score():
        break
    else:
        if check_win() is not None:
            x = check_win()
            board[x] = True
            print(x)
            available_moves.pop(available_moves.index(x))
            check_score()
            break
        else:
            if check_threat() is not None:
                x = check_threat()
                board[x] = True
                print("Computer played: " + x)
                available_moves.pop(available_moves.index(x))
            else:
                if check_double_attack() is not None:
                    x = check_double_attack()
                    board[x] = True
                    print("Computer played: " + x)
                    available_moves.pop(available_moves.index(x))
                else:
                    list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    while True:
                        x = random.choice(list1)
                        if x in available_moves:
                            break
                        else:
                            list1.pop(list1.index(x))
                    board[x] = True
                    print("Computer played: " + x)
                    available_moves.pop(available_moves.index(x))
    time.sleep(3)
