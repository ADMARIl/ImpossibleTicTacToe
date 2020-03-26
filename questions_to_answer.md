# (1) Minimax 

(b) When AI always moves first, it has the advantage. Run the program a few times. Do you ever win?  To make it a little more interesting, use the random package to randomly choose a move for human before AI makes its first move.  Run the program a few more times.  Do you ever win?  Any difference in behavior when the human has the first move?

- In my time playing the game, I have never won. At most a draw. In fact, most of the time the AI won. 
- When the ai is changed to have the human randomly move first, I found I was able to win once in the time I spent playing. The behavior this time around seemed less dominant, rather that it was playing not to win but in fact not to lose.

(c) What is the worst case time complexity for a 3 x 3 Tic-Tac-Toe game? Why?

## Write your answer here

# (2) Heuristics for CSP 

(a) We covered several heuristics for CSP search. Explain why when selecting a variable to assign a value next, it is good to choose the variable that is most constrained, but the value that is least constraining.

- By picking the variable that is the most constrained you ensure that the most efficient solution is found. By picking the least constraining value you ensure that all the other values are available

# (3) Magic Squares 

(b ) Note that the MinConflicts() solver fails to solve even the smallest problem. Think about how this strategy works and explain why MinConflicts() does not work well for this problem.

- For this problem type, there is no possible way to 'minimize' the problem (i.e. you either have the sum or you do not)

(c) Can you get a solution for a magic square of size six using any of the solvers and if so, how long does it take? Do you think that using CSP is a good approach for generating magic squares? Why or why not.

- MinConflicts solver does not generate a solution
- Backtracking solver does generate a solution
- RecursiveBacktracking does not generate a solution


> For this assignment I collaborated with [Chase Carbaugh](https://github.com/chasec1)

