#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;

// ------------------------------------------------------------------
// DECLARATION OF VARIABLES------------------------------------------
// ------------------------------------------------------------------

string winning_lines[8][3] = {{"1", "2", "3"}, {"4", "5", "6"}, {"7", "8", "9"}, {"1", "4", "7"}, {"2", "5", "8"}, {"3", "6", "9"}, {"1", "5", "9"}, {"3", "5", "7"}};
string available_moves[10] = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
map <string,int> board = {{"1", 0}, {"2", 0}, {"3", 0}, {"4", 0}, {"5", 0}, {"6", 0}, {"7", 0} ,{"8", 0}, {"9", 0}};


// ------------------------------------------------------------------
// FUNCTIONS---------------------------------------------------------
// ------------------------------------------------------------------
void display_board(map <string, int> board){
    for(int i = 0; i < 3; i++){
        string str1 = "";
        for (int j = 0; j < 3; j++){
            if (board[to_string(3 * i + j + 1)] == 1) str1 += "O ";
            else if (board[to_string(3 * i + j + 1)] == 2) str1 += "X ";
            else if (board[to_string(3 * i + j + 1)] == 0) str1 += "_ ";
        }
        cout << str1 << endl;
    }
}


bool check_score(){
    bool abool = true;
    for (int i = 0; i < 8; i++){
        if (board[winning_lines[i][0]] == true and (board[winning_lines[i][1]] == true and board[winning_lines[i][2]] == true)){
            cout << "Computer won!" << endl;
            abool = false;
            return true;
        }
        
        else if (board[winning_lines[i][0]] == false and board[winning_lines[i][1]] == false and board[winning_lines[i][2]] == false){
            cout << "You won!" << endl;
            abool = false;
            return true;
        }
        
        if (abool == true){
            bool bbool = true;
            for (int i = 0; i < 9; i++){
                if (board[to_string(i + 1)] == 0){
                    bbool = false;
                }
            }
            if (bbool == true){
                cout << "Draw!" << endl;
                return true;
            }
        }
    }
    return false;
}

string check_win(){
    for (int i = 0; i < 8; i++){
        if (board[winning_lines[i][0]] == 1 and board[winning_lines[i][1]] == 1 and board[winning_lines[i][2]] == 0){
            return winning_lines[i][2];
        }
        else if (board[winning_lines[i][0]] == 1 and board[winning_lines[i][2]] == 1 and board[winning_lines[i][1]] == 0){
            return winning_lines[i][1];
        }
        else if (board[winning_lines[i][1]] == 1 and board[winning_lines[i][2]] == 1 and board[winning_lines[i][0]] == 0){
            return winning_lines[i][0];
        }
    }
    return "0";
}
    
    
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
        
        
        
        int main(){
            // ------------------------------------------------------------------
            // INSTRUCTIONS FOR PLAYER-------------------------------------------
            // ------------------------------------------------------------------
            
            cout << " This tic tac toe AI Machine has been created by AJR07, Collaborated by YNWAPythoner. 23 Nov 2020" << '\n' << "*********TO REQUEST MORE FEATURES/REPORT A BUG, PLEASE LEAVE A NOTE ON GITHUB. *******" << '\n' << "To play with the program, please input the place you would want to place your X" << '\n';
            usleep(1000000);
            cout <<  "It is defined by (row character)(column number)" << '\n' << "This is the board:" << '\n' << "1 2 3" << '\n' << "4 5 6" << '\n' << "7 8 9" << '\n';
            usleep(1000000);
            cout <<  "The indexes are what you are supposed to enter to select a move later on" << '\n' << "The player would be X all the time, whether he moves first or not. (Could be changed in the future)" << '\n';
            usleep(5000000);
            
            // ------------------------------------------------------------------
            // INPUTS------------------------------------------------------------
            // ------------------------------------------------------------------
            
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
                                                                            }
}
