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
    if check_player(ai) == ai:
        return ai
    elif check_player(human) == human:
        return human
    else:
        return 0


def check_player(player):
    if ((board[0][0] == player and board[1][0] == player and board[2][0] == player) or  # left
            (board[0][1] == player and board[1][1] == player and board[2][1] == player) or  # center
            (board[0][2] == player and board[1][2] == player and board[2][2] == player) or  # right
            (board[0][0] == player and board[0][1] == player and board[0][2] == player) or  # top
            (board[1][0] == player and board[1][1] == player and board[1][2] == player) or  # middle
            (board[2][0] == player and board[2][1] == player and board[2][2] == player) or  # bottom
            (board[0][0] == player and board[1][1] == player and board[2][2] == player) or  # tl to br diag
            (board[2][0] == player and board[1][1] == player and board[0][2] == player)):  # bl to tr diag
        return player
    else:
        return 0


def check_stalemate():
    # check if the board is full and the game is over
    is_stalemate = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '':
                is_stalemate = False
    return is_stalemate


def minimax(m_board, depth, isMaximizing):
    # ###################Your code here####################
    # Your implementation of minimax
    # Recursively alternates between min and max
    # #####################################################

    curr_board = copy.deepcopy(m_board)
    # check if the current board state is a terminal state
    player = ai
    if ((curr_board[0][0] == player and curr_board[1][0] == player and curr_board[2][0] == player) or  # left
            (curr_board[0][1] == player and curr_board[1][1] == player and curr_board[2][1] == player) or  # center
            (curr_board[0][2] == player and curr_board[1][2] == player and curr_board[2][2] == player) or  # right
            (curr_board[0][0] == player and curr_board[0][1] == player and curr_board[0][2] == player) or  # top
            (curr_board[1][0] == player and curr_board[1][1] == player and curr_board[1][2] == player) or  # middle
            (curr_board[2][0] == player and curr_board[2][1] == player and curr_board[2][2] == player) or  # bottom
            (curr_board[0][0] == player and curr_board[1][1] == player and curr_board[2][
                2] == player) or  # tl to br diag
            (curr_board[2][0] == player and curr_board[1][1] == player and curr_board[0][
                2] == player)):  # bl to tr diag
        return depth
    player = human
    if ((curr_board[0][0] == player and curr_board[1][0] == player and curr_board[2][0] == player) or  # left
            (curr_board[0][1] == player and curr_board[1][1] == player and curr_board[2][1] == player) or  # center
            (curr_board[0][2] == player and curr_board[1][2] == player and curr_board[2][2] == player) or  # right
            (curr_board[0][0] == player and curr_board[0][1] == player and curr_board[0][2] == player) or  # top
            (curr_board[1][0] == player and curr_board[1][1] == player and curr_board[1][2] == player) or  # middle
            (curr_board[2][0] == player and curr_board[2][1] == player and curr_board[2][2] == player) or  # bottom
            (curr_board[0][0] == player and curr_board[1][1] == player and curr_board[2][
                2] == player) or  # tl to br diag
            (curr_board[2][0] == player and curr_board[1][1] == player and curr_board[0][
                2] == player)):  # bl to tr diag
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
    print()


def find_best_move():
    # ###################Your code here####################
    # Finds the best move for AI starts the minimax recursion
    # #####################################################

    if check_for_winner() != 0 or check_stalemate():
        return [-1, -1]
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
    best_move_val = minimax(best_move_board, 0, True)  # this could be positive infinity?
    # check all the empty cells to see if they are the best move
    for move in cells:
        # print(move)
        # crete a temporary board that we can put the move into
        curr_board = copy.deepcopy(board)
        curr_board[move[0]][move[1]] = ai
        curr_value = minimax(curr_board, 0, True)
        # print(curr_value)
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

    while check_for_winner() == 0 and not check_stalemate():
        usr_input = input("Which cell would you like to put an 'O' in?  starting from top left:0,0 0,1 0,2 1,0 1,1 1,"
                          "2 2,0 2,1 2,2\n")
        board[int(usr_input[0])][int(usr_input[2])] = human
        if check_for_winner() != 0 or check_stalemate():
            print_board()
            break
        else:
            new_x, new_y = find_best_move()
            board[new_x][new_y] = ai
            print_board()

    if check_for_winner() != 0:
        print("Winner is", check_for_winner())
    else:
        print("Stalemate reached. No winner.")


# Calls on main
main()
