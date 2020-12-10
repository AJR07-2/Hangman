#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;

// ------------------------------------------------------------------
// DECLARATION OF VARIABLES------------------------------------------
// ------------------------------------------------------------------

string winning_lines[8][3] = {{"1", "2", "3"}, {"4", "5", "6"}, {"7", "8", "9"}, {"1", "4", "7"}, {"2", "5", "8"}, {"3", "6", "9"}, {"1", "5", "9"}, {"3", "5", "7"}};
string available_moves[10] = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
map <string,int> board = {{"1", 0}, {"2", 0}, {"3", 0}, {"4", 0}, {"5", 0}, {"6", 0}, {"7", 0} ,{"8", 0}, {"9", 0}};
int selection;

// ------------------------------------------------------------------
// FUNCTIONS---------------------------------------------------------
// ------------------------------------------------------------------
void display_board(){
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
    return "000";
}


int check_double_attack(){
    int length = 0;
    for(int i = 0; i < 10; i++){
        if(available_moves[i] != "0"){
            break;
        }
        else{
            length++;
        }
    }
    for (int j = 0; j < length; j++){
        map<string, int> pseudo_board = board;
        pseudo_board[to_string(j)] = 1;
        long long counter = 0;
        for (int i = 0; i < 8; i++){
            if (pseudo_board[winning_lines[i][0]] == 1 and pseudo_board[winning_lines[i][1]] == 1 and pseudo_board[winning_lines[i][2]] == 0){
                counter += 1;
            }
            else if (pseudo_board[winning_lines[i][0]] == 1 and pseudo_board[winning_lines[i][2]] == 1 and pseudo_board[winning_lines[i][1]] == 0){
                counter += 1;
            }
            else if (pseudo_board[winning_lines[i][1]] == 1 and pseudo_board[winning_lines[i][2]] == 1 and pseudo_board[winning_lines[i][0]] == 0){
                counter += 1;
            }
        }
        if (counter >= 2){
            return j;
        }
    }
    return -1;
}


string check_threat(){
    for(int i = 0; i <8; i++){
        if (board[winning_lines[i][0]] == 2 and board[winning_lines[i][1]] == 2 and board[winning_lines[i][2]] == 0){
            return winning_lines[i][2];
        }
        else if (board[winning_lines[i][0]] == 2 and board[winning_lines[i][2]] == 2 and board[winning_lines[i][1]] == 0){
            return winning_lines[i][1];
        }
        else if (board[winning_lines[i][1]] == 2 and board[winning_lines[i][2]] == 2 and board[winning_lines[i][0]] == 0){
            return winning_lines[i][0];
        }
    }
    return "000";
}

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
    cout << "Do you want to go first or second? (1 for first and 2 for second): ";
    usleep(2000000);
    int choice; cin >> choice;
    if (choice == 2){
        board["5"] = true;
        cout << "Computer played: 5";
        available_moves[5]
    }
    booly = True
    while (true){
        display_board();
        cout << "Enter your choice";
        cin >> selection;
        string x = to_string(selection); int choice  = x[0] - '0';
        board[x] = 2;
        available_moves[choice] = "0";
        if (check_score()){
            break;
        }
        else{
            if (check_win() != "000"){
                x = check_win();
                board[x] = true;
                choice  = x[0] - '0';
                cout << "x" << '\n';
                available_moves[choice] = "0";
                check_score();
                break;
            }
            else{
                if (check_threat() != "000"){
                    x = check_threat();
                    board[x] = true;
                    choice  = x[0] - '0';
                    cout << "Computer played: " << x << '\n';
                    available_moves[choice] = "0";
                }
                
                else{
                    if (check_double_attack() != -1){
                        x = check_double_attack();
                        board[x] = true;
                        choice  = x[0] - '0';
                        cout << "Computer played: " << x << '\n';
                        available_moves[choice] = "0";
                    }
                    else{
                        string list1[10] = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
                        while (true){
                            x = list1[rand()%10];
                            bool c = true;
                            for(int i = 0; i < 10; i++){
                                if(x == available_moves[i] and available_moves[i]!= "0"){
                                    c = false;
                                    break;
                                }
                            }
                            if (c == false){
                                break;
                            }
                            else{
                                choice  = x[0] - '0'-1;
                                list1[choice] = "0";
                            }
                        }
                        board[x] = 1;
                        cout << "Computer played: " << x << '\n';
                        choice  = x[0] - '0'-1;
                        available_moves[choice] = "0";
                    }
                }
            }
        }
        usleep(3000000);
    }
}
