# N-Queens-Solver
This is a Python implementation of the NQueens game.
The game consists of placing N chess queens on an NxN chessboard so that no two queens threaten each other.
Queens can move horizontally, vertically, and diagonally with no limit on distance.


## ChessBoard class
The ChessBoard class represents the chessboard on which the game is played.
It has the following methods:
### __init__(self): Initializes the board with empty spaces.
### ValidValue(self,X,Y): Checks if a given position is valid and does not violate any rules.
### UpdateBoard(self,X,Y): Places a queen on the board at the given position.
### PrintBoard(self): Prints the current state of the board.
### IsWinner(self): Checks if all queens have been placed on the board without violating any rules.

## NqueensSolver
The NqueensSolver class solves the NQueens game using a backtracking algorithm.
It has the following methods:
### __init__(self): Initializes the solver with an empty list of solutions and an empty set of visited boards.
### Solver(self,board): Tries to place a queen on each square of the board using backtracking.
### PrintSolutions(self): Prints all solutions found.

## GameRunning
The GameRunning class runs the NQueens game. 
It has the following methods:
### __init__(self): Initializes the game with a new chessboard and sets gamerunning to True.
### StartGame(self): Prompts the user to choose between playing themselves or using the solver.


## Usage
To play the game, run GameRunning.py. You will be prompted to choose between playing yourself or using the solver. 
If you choose to play yourself, enter the x and y coordinates of each move. If you choose to use the solver, all solutions will be printed.
