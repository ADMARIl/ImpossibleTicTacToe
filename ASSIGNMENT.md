# Homework 3 - Minimax and CSP Exercises
# Due March 25, 2020
## Total Points 200

Note:  You may collaborate with others for this homework to work through any issues you may encounter but you must turn in your own work and you must list who you collaborated with.  Collobrations should not be larger than a team of 3 people.

## Minimax (120)
You will create your version of Tic-Tac-Toe for a 3 x 3 game board using the minimax algorithm.  Tic-Tac-Toe can be implemented in different ways but we are going to implement a simple version so you can get a feel for how the minimax algorithm is used for games.  

## CSP (80)
You will explore the Magic Squares problem using the Constraints package that we reviewed in class.  You will also explore  some of the heuristics we reviewed in class.


## Directions:

(1) Minimax (120)

(a) (100) Create your version of Tic-Tac-Toe for a 3 x 3 game board using the Minimax algorithm. Use the starter code named tictactoe.py. Write the program such that it is simulating the AI.  AI's moves are represented by 'X' and the opponents moves are represented by 'O'.  Using the command line, take input from your opponent that indicates where they would like to move (i.e. 0,0 0,1 0,2 1,0 1,1 1,2 2,0 2,1 2,2).  Run your minimax algorithm to determine the best move for AI.  Once a move is made, update the board and display the board to the user.  Check for a winner after each move and end the game if there is a winner or a tie.  Have AI move first. 

Use the following scores:
scores = {'X': 10,'O': -10,'tie': 0}

(b) (10) When AI always moves first, it has the advantage. Run the program a few times. Do you ever win?  To make it a little more interesting, use the random package to randomly choose a move for human before AI makes its first move.  Run the program a few more times.  Do you ever win?  Any difference in behavior when the human has the first move?


(c)(10) What is the worst case time complexity for a 3 x 3 Tic-Tac-Toe game? Why?

(2) Heuristics for CSP  (20) 

(a) (20) We covered several heuristics for CSP search. Explain why when selecting a variable to assign a value next, it is good to choose the variable that is most constrained, but the value that is least constraining.  

(3)  Magic Squares (60)
In class we showed examples of using the python constraint package to generate magic squares of size three. In general, there is always a magic square of size N whose magic sum is equal to N\*(N\*\*2+1)/2 for n>2. (Others may also exist.)

(a) (25) Complete a file ms.py (we included a version of ms.py from class, you will need th change this file) that defines a subclass named MS of the constraints Problem class to find a magic square of a given size with a given solver. You can test this directly like this:

  ```
  myhw3> python
  >>> import ms
  >>> ms.MS(3).getSolution()
  {0: 6, 1: 7, 2: 2, 3: 1, 4: 5, 5: 9, 6: 8, 7: 3, 8: 4}
  ```

(b ) (25) Note that the MinConflicts() solver fails to solve even the smallest problem. Think about how this strategy works and explain why MinConflicts() does not work well for this problem.

(c) (10) Can you get a solution for a magic square of size six using any of the solvers and if so, how long does it take? Do you think that using CSP is a good approach for generating magic squares? Why or why not.


## What to turn in
Commit everything into github.  You will turn in the tictactoe.py file, the ms.py file, and the questions_to_answer.md file with answers to the questions outlined in this README.md file.

