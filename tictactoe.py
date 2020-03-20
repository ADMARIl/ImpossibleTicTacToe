# #######################################
# HW 3 Tic-Tac-Toe MiniMax Algorithm
# Inspiration from AIMA,Russell,Novig, Shiffman
# ######################################
# positive infinity
p_inf = float("inf")
# negative infinity
n_inf = float("-inf")

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

scores = {'X': 10, 'O': -10, 'tie': 0}
ai = 'X'
human = 'O'
currentPlayer = human


def check_for_winner():
    # ###################Your code here####################
    # Code that checks for a winner
    # #####################################################
    player = ai
    if ((board[0][0] == player and board[1][0] == player and board[2][0]) or  # left
            (board[0][1] == player and board[1][1] == player and board[2][1]) or  # center
            (board[0][2] == player and board[1][2] == player and board[2][2]) or  # right
            (board[0][0] == player and board[0][1] == player and board[0][2]) or  # top
            (board[1][0] == player and board[1][1] == player and board[1][2]) or  # middle
            (board[2][0] == player and board[2][1] == player and board[2][2]) or  # bottom
            (board[0][0] == player and board[1][1] == player and board[2][2]) or  # tl to br diag
            (board[2][0] == player and board[1][1] == player and board[0][2])):  # bl to tr diag
        return player
    player = human
    if ((board[0][0] == player and board[1][0] == player and board[2][0]) or  # left
            (board[0][1] == player and board[1][1] == player and board[2][1]) or  # center
            (board[0][2] == player and board[1][2] == player and board[2][2]) or  # right
            (board[0][0] == player and board[0][1] == player and board[0][2]) or  # top
            (board[1][0] == player and board[1][1] == player and board[1][2]) or  # middle
            (board[2][0] == player and board[2][1] == player and board[2][2]) or  # bottom
            (board[0][0] == player and board[1][1] == player and board[2][2]) or  # tl to br diag
            (board[2][0] == player and board[1][1] == player and board[0][2])):  # bl to tr diag
        return player
    else:
        return False


def minimax(board, depth, isMaximizing):
    # ###################Your code here####################
    # Your implementation of minimax
    # Recursively alternates between min and max
    # #####################################################
    curr_board = board

    # see what cells are empty
    cells = []
    for i in range(len(curr_board)):
        for j in range(len(curr_board[i])):
            if curr_board[i][j] == '':
                cells.append([i, j])

    # minimax all the empty cells
    for loc in cells:
        curr_board[loc[0]][loc[1]] = ai
        rank = minimax(curr_board, depth - 1, not isMaximizing)

    print(board, depth, isMaximizing)


def print_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' | ')
        if i + 1 != len(board):
            print("==============")


def find_best_move():
    # ###################Your code here####################
    # Finds the best move for AI starts the minimax recursion
    # #####################################################

    minimax(board, 1, True)


def main():
    # ###################Your code here####################
    # Have 'X' make the first move.
    # In a loop
    # Display the board
    # Read in input from the command line to
    # determine where 'O' would like to move.
    # After 'O' makes his move, run your minimax
    # algorithm to decide where 'X' should move.
    # After every move print the current state of the board
    # After every move check for a winner.
    # #####################################################

    print("AI moves first!")
    find_best_move()
    print_board()

    while not check_for_winner():
        print("test")


# Calls on main
main()
