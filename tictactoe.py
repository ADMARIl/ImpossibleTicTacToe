# #######################################
# HW 3 Tic-Tac-Toe MiniMax Algorithm
# Inspiration from AIMA,Russell,Novig, Shiffman
# ######################################
import copy
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
    return 0


def minimax(m_board, depth, isMaximizing):
    # ###################Your code here####################
    # Your implementation of minimax
    # Recursively alternates between min and max
    # #####################################################
    curr_board = copy.deepcopy(m_board)
    # value = 1
    # check if the current board state is a terminal state
    player = ai
    if ((curr_board[0][0] == player and curr_board[1][0] == player and curr_board[2][0]) or  # left
            (curr_board[0][1] == player and curr_board[1][1] == player and curr_board[2][1]) or  # center
            (curr_board[0][2] == player and curr_board[1][2] == player and curr_board[2][2]) or  # right
            (curr_board[0][0] == player and curr_board[0][1] == player and curr_board[0][2]) or  # top
            (curr_board[1][0] == player and curr_board[1][1] == player and curr_board[1][2]) or  # middle
            (curr_board[2][0] == player and curr_board[2][1] == player and curr_board[2][2]) or  # bottom
            (curr_board[0][0] == player and curr_board[1][1] == player and curr_board[2][2]) or  # tl to br diag
            (curr_board[2][0] == player and curr_board[1][1] == player and curr_board[0][2])):  # bl to tr diag
        return depth
    player = human
    if ((curr_board[0][0] == player and curr_board[1][0] == player and curr_board[2][0]) or  # left
            (curr_board[0][1] == player and curr_board[1][1] == player and curr_board[2][1]) or  # center
            (curr_board[0][2] == player and curr_board[1][2] == player and curr_board[2][2]) or  # right
            (curr_board[0][0] == player and curr_board[0][1] == player and curr_board[0][2]) or  # top
            (curr_board[1][0] == player and curr_board[1][1] == player and curr_board[1][2]) or  # middle
            (curr_board[2][0] == player and curr_board[2][1] == player and curr_board[2][2]) or  # bottom
            (curr_board[0][0] == player and curr_board[1][1] == player and curr_board[2][2]) or  # tl to br diag
            (curr_board[2][0] == player and curr_board[1][1] == player and curr_board[0][2])):  # bl to tr diag
        return depth
    # find the empty cells in our current board
    cells = []
    for i in range(len(curr_board)):
        for j in range(len(curr_board[i])):
            if curr_board[i][j] == '':
                cells.append([i, j])
    # MAX
    if isMaximizing:
        best_val = n_inf
        for move in cells:
            # create a deep copy of the current board so we can recurse with it
            curr_board_nest = copy.deepcopy(curr_board)
            curr_board_nest[move[0]][move[1]] = ai
            # recurse
            value = minimax(curr_board_nest, depth + 1, False)
            best_val = max(best_val, value)
        return best_val
    # MIN
    else:
        best_val = p_inf
        for move in cells:
            curr_board_nest = copy.deepcopy(curr_board)
            curr_board_nest[move[0]][move[1]] = ai
            # recurse
            value = minimax(curr_board_nest, depth + 1, True)
            best_val = min(best_val, value)
        return best_val


def print_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="")
            if j + 1 != len(board[i]):
                print("  |  ", end="")
        if i + 1 != len(board):
            print("\n==============")


def find_best_move():
    # ###################Your code here####################
    # Finds the best move for AI starts the minimax recursion
    # #####################################################

    # find all the empty cells
    cells = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '':
                cells.append([i, j])
    # create our starting best move to compare against
    best_move_board = copy.deepcopy(board)
    x, y = cells[0]
    best_move_board[x][y] = ai
    best_move = cells[0]
    best_move_val = minimax(best_move_board, 0, True)
    # check all the empty cells to see if they are the best move
    for move in cells:
        print(move)
        # crete a temporary board that we can put the move into
        curr_board = copy.deepcopy(board)
        curr_board[move[0]][move[1]] = ai
        curr_value = minimax(curr_board, 0, True)
        print(curr_value)
        # if the minimax tells us the current move is better, update the best move
        if curr_value < best_move_val:
            best_move = move
    return best_move


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
    new_x, new_y = find_best_move()
    board[new_x][new_y] = ai
    print_board()

    # while not check_for_winner():
     #   print("test")


# Calls on main
main()
