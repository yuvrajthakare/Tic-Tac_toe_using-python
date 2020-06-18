board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

game_is_still_running = True

current_player = "X"

winner = None

def play_game():
    
      
    

    while game_is_still_running:
        display_board()
        
        handle_turn(current_player)

        check_if_game_over()


        filp_player()

    display_board()
    if winner=="X" or winner == "O":
        print(winner + "  Won.")
    elif winner == None:
        print("Tie.")
        

        
    
def handle_turn(current_player):
    print(current_player + "'S turn ")
    position = int(input("enter the position from 1-9 :"))

    valid = False

    while not valid:
        
        while position not in range(1,10):
            position = int(input("enter the position from 1-9 :"))
        
        if board[position-1] == "-":
            valid =  True
        else:
            print("you can't go there go again")
            position = None
        
             
    board[position-1] = current_player
    return

def check_if_game_over():
    check_for_winner()
    check_for_tie()
    return
def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner :
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_for_tie():
    global game_is_still_running
    if "-" not in board:
        game_is_still_running = False

def check_rows():
    global game_is_still_running
    row_1 =  board[0]==board[1]==board[2] != "-"
    row_2 =  board[3]==board[4]==board[5] != "-"
    row_3 =  board[6]==board[7]==board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_still_running = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    
    return

def check_columns():
    global game_is_still_running
    column_1 =  board[0]==board[3]==board[6] != "-"
    column_2 =  board[1]==board[4]==board[7] != "-"
    column_3 =  board[2]==board[5]==board[8] != "-"

    if column_1 or column_2 or column_3:
        game_is_still_running = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    
    return

def check_diagonals():
    global game_is_still_running
    diagonal_1 =  board[0]==board[4]==board[8] != "-"
    diagonal_2 =  board[2]==board[4]==board[6] != "-"

    if diagonal_1 or diagonal_2 :
        game_is_still_running = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def display_board():
    print(" | " , board[0] + " | ",board[1] + " | ",board[2] + " | ")
    print(" | " , board[3] + " | ",board[4] + " | ",board[5] + " | ")
    print(" | " , board[6] + " | ",board[7] + " | ",board[8] + " | ")

def filp_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()
        
