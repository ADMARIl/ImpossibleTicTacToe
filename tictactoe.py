# #######################################
# HW 3 Tic-Tac-Toe MiniMax Algorithm
# Inspiration from AIMA,Russell,Novig, Shiffman
# ######################################
import copy
import random

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

# only one of these can be true at once
random_human_first_move = False
ai_first = True


def check_for_winner():
    # ###################Your code here####################
    # Code that checks for a winner
    # #####################################################
    if check_player(ai, board) == ai:
        return ai
    elif check_player(human, board) == human:
        return human
    else:
        return 0


def check_player(player, c_board):
    # check if the provided player won on the given board
    if ((c_board[0][0] == player and c_board[1][0] == player and c_board[2][0] == player) or  # left
            (c_board[0][1] == player and c_board[1][1] == player and c_board[2][1] == player) or  # center
            (c_board[0][2] == player and c_board[1][2] == player and c_board[2][2] == player) or  # right
            (c_board[0][0] == player and c_board[0][1] == player and c_board[0][2] == player) or  # top
            (c_board[1][0] == player and c_board[1][1] == player and c_board[1][2] == player) or  # middle
            (c_board[2][0] == player and c_board[2][1] == player and c_board[2][2] == player) or  # bottom
            (c_board[0][0] == player and c_board[1][1] == player and c_board[2][2] == player) or  # tl to br diag
            (c_board[2][0] == player and c_board[1][1] == player and c_board[0][2] == player)):  # bl to tr diag
        return player
    else:
        return 0


def check_stalemate(stale_board=None):
    # check if the board is full and the game is over
    if stale_board is None:
        stale_board = board
    is_stalemate = True
    for i in range(len(stale_board)):
        for j in range(len(stale_board[i])):
            if stale_board[i][j] == '':
                is_stalemate = False
    return is_stalemate


def minimax(m_board, depth, isMaximizing):
    # ###################Your code here####################
    # Your implementation of minimax
    # Recursively alternates between min and max
    # #####################################################

    curr_board = copy.deepcopy(m_board)
    # check if the current board state is a terminal state
    if check_player(ai, curr_board) == ai:
        return scores[ai]
    elif check_player(human, curr_board) == human:
        return scores[human]
    elif check_stalemate(curr_board):
        return scores['tie']
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
            curr_board_nest[move[0]][move[1]] = ''
            best_val = max(best_val, value)
        # print(best_val)
        return best_val
    # MIN
    else:
        best_val = p_inf
        for move in cells:
            curr_board_nest = copy.deepcopy(curr_board)
            curr_board_nest[move[0]][move[1]] = human
            # recurse
            value = minimax(curr_board_nest, depth + 1, True)
            curr_board_nest[move[0]][move[1]] = ''

            best_val = min(best_val, value)
        # print(best_val)
        return best_val


def print_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="")
            if board[i][j] == '':
                print(" ", end="")
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
        print("this shouldn't happen")
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
    best_move_val = n_inf  # this could be positive infinity?
    # check all the empty cells to see if they are the best move
    for move in cells:
        # print(move)
        # crete a temporary board that we can put the move into
        curr_board = copy.deepcopy(board)
        curr_board[move[0]][move[1]] = ai
        curr_value = minimax(curr_board, 0, False)
        # print(curr_value)
        # if the minimax tells us the current move is better, update the best move
        if curr_value > best_move_val:
            # print(best_move, "has been usurped by", move)
            best_move_val = curr_value
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

    # do we make a random move for the human first?
    if random_human_first_move and not ai_first:
        print("Random Human Move!")
        board[random.randint(0, 2)][random.randint(0, 2)] = human
        print_board()
    # does the ai move first?
    elif ai_first and not random_human_first_move:
        print("AI moves!")
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
