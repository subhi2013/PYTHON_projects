board = [" "," "," ",
         " "," "," ",
         " "," "," "]
def display_board():
    print(board[0], "|",board[1], "|", board[2])
    print("--------------")
    print(board[3], "|", board[4], "|" , board[5])
    print("--------------")
    print(board[6], "|" , board[7], "|" , board[8])
def check_winner():
    if board[0] == board[1] == board[2] != " ":
        return True
    elif board[3] == board[4] == board[5] != " ":
        return True
    elif board[6] == board[7] == board[8] != " ":
        return True
    elif board[0] == board[3] == board[6] != " ":
        return True
    elif board[1] == board[4] == board[7] != " ":
        return True
    elif board[2] == board[5] == board[8] != " ":
        return True
    elif board[0] == board[4] == board[8] != " ":
        return True
    elif board[2] == board[4] == board[6] != " ":
        return True
    return False
current_player = "x"
for turn in range(9):
    display_board()
    position = int(input("player" + current_player + 
    ",enter position(0-8):"))
    if board[position] == " ":
        board[position] = current_player
        if check_winner():
            display_board()
            print(current_player, "wins")
            break
        if current_player == "x":
            current_player = "o"
        else:
            current_player = "x"
    else:
        print("position already taken")
        if not check_winner():
            print("its a draw")
    play_again = input("play again (yes/no):")
    if play_again == "yes":
        print("starting new game....")
    else:
        print("thanks for playing")