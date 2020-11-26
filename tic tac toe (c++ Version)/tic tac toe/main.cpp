#include <bits/stdc++.h>
using namespace std;
int tictactoe[3][3];
string ans;
int main() {
    //CURRENTLY RELIES ON CORRECT INPUTS FROM THE USER
    //MARK: Instructions for player
    cout << "This tic tac toe AI Machine has been created by AJR07, 23 Nov 2020" << endl;
    cout << "*********TO REQUEST MORE FEATURES/RSPORT A BUG, PLEASE LEAVE A NOTE ON GITHUB. *******" << endl;
    cout<< "To play with the program, please input the place you would want to place your X or 0" << endl;
    cout << "It is defined by (row character)(column number)" << endl;
    cout << "a1 a2 a3" << endl << "b1 b2 b3" << endl << "c1 c2 c3" << endl;
    //MARK: Inputs
    cout << "Would you like to go first? (Input Yes/No)" << endl;
    cin >> ans;
    
    if (ans == "Yes"){
        cout << "Alright, you are X" << endl;
        cout << "Which square do you want to put your";
    }
    else{
        cout << "Alright, you are O" << endl;
    }
    
    
    
    //TODO: Winner? Threat? Move
}


