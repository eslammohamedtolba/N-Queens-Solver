# Importing the ChessBoard and NqueensSolver classes
from ChessBoard import *
from NQueensSolver import *

# Defining the GameRunning class
class GameRunning:
    def __init__(self):
        self.board = ChessBoard()
        self.gamerunning=True
    
    def StartGame(self):
        # Printing the initial state of the chessboard
        self.board.PrintBoard()
        
        # Prompting the user to choose between playing themselves or using the solver
        while True:
            print("Do you want to solve it with yourself(0) or want Solver(1) to solve it?: ",end = "")
            anySolver = int(input())
            if anySolver in [0,1]:
                break

        if anySolver==0:
            # If the user chooses to play themselves
            while True:
                x = int(input(f"Enter x-axis: "))
                y = int(input(f"Enter y-axis: "))
                if self.board.UpdateBoard(x,y):
                    self.board.PrintBoard()
                    if self.board.IsWinner():
                        print("You won!")
                        break
                else:
                    print("Invalid play")
        else:
            # If the user chooses to use the solver
            solver = NqueensSolver()
            solver.Solver(self.board)
            solver.PrintSolutions()
