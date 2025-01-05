def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    #check rows, columns and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
         return True
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"player {current_player}, enter the row (0, 1, or 2):"))
        col = int(input(f"player {current_player}, enter the column (0, 1, or 2):"))

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"player {current_player} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X' 
        else:
            print("Cell is already taken, Try again.")

tic_tac_toe()