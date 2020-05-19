#TIC TAC TOE - Challenge 1
#Udemy Challenge 1



def display_board(): #outlines the board, with positions correlating to list

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |\n')

def player_choice(): #Lets user choose a marker, returns choice.
    mark = " "
    chosen = False
    
    while chosen == False:
        mark = input("Player 1 , would you like to be X or O? ").upper()
        if mark == 'X':
            return ('X', 'O')
            chosen = True
        if mark == 'Y':
            return ('O', 'X')
            chosen = True
        else:
            print('invald. Please try again.')
            chosen = False


def player_1():

        position = int(input("Player 1, make your move: "))
        board[position] = player1
        display_board()

def player_2():

        position = int(input("Player 2, make your move: "))
        board[position] = player2

        display_board()
        win_check(board, player2)


def win_check(board, mark):
    if ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)):

        if mark == 'X':
            print ("Player X Wins!")

        else:
            print ("Player O Wins!")

        return True


while True:
    print("Welcome to Tic Tac Toe!\n")
    board = ['#','1','2','3','4','5','6','7','8','9']
    display_board()
    player1, player2 = player_choice()
    game_on = True

    while game_on == True:
        player_1()
        if win_check(board, player1) == True:
            again= input("Would you like to repay? Y or N: ")

            if again == "Y":
                break
            else:
                game_on = False
                exit()                
        else:
            player_2()

            if win_check(board, player_2) == True:
                again= input("Would you like to repay? Y or N: ")

                if again == "Y":
                    break
                else:
                    exit()
            
    
    

