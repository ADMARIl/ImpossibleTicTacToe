########################################
# HW 3 Tic-Tac-Toe MiniMax Algorithm
# Inspiration from AIMA,Russell,Novig, Shiffman
#######################################
# positive infinity
p_inf = float("inf")
# negative infinity
n_inf = float("-inf")

board = [
  ['', '', ''],
  ['', '', ''],
  ['', '', '']

];

scores = {'X': 10,'O': -10,'tie': 0}
ai = 'X'
human = 'O'
currentPlayer = human

def check_for_winner():
 ####################Your code here####################
 # Code that checks for a winner
 ######################################################


def minimax(board, depth, isMaximizing):
 ####################Your code here####################
 # Your implementation of minimax
 # Recursively alternates between min and max
 ######################################################



def find_best_move():
 ####################Your code here####################
 # Finds the best move for AI starts the minimax recursion
 ######################################################


def main ():
 ####################Your code here####################
 # Have 'X' make the first move.
 # In a loop
 # Display the board
 # Read in input from the command line to 
 # determine where 'O' would like to move.
 # After 'O' makes his move, run your minimax 
 # algorithm to decide where 'X' should move.
 # After every move print the current state of the board
 # After every move check for a winner.
 ######################################################

#Calls on main
main()

