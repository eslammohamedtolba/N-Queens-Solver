# Importing the deepcopy function from the copy module
from copy import deepcopy

# Defining the NqueensSolver class
class NqueensSolver:
    def __init__(self):
        self.Solutions = []
        self.VisitedBoards = set()

    def Solver(self,board):
        # If a solution is found, check if it has already been visited
        if board.IsWinner():
            if str(board.Board) not in self.VisitedBoards:
                self.Solutions.append(deepcopy(board))
                self.VisitedBoards.add(str(board.Board))
                return
        # Try to place a queen on each square of the board
        for IndexRow in range(1,board.SizeBoard+1):
            for IndexCol in range(1,board.SizeBoard+1):
                if board.UpdateBoard(IndexRow,IndexCol):
                    self.Solver(board)
                    board.Board[IndexRow-1][IndexCol-1]=' '

    # Print all solutions found
    def PrintSolutions(self):
        for solution in self.Solutions:
            solution.PrintBoard()

