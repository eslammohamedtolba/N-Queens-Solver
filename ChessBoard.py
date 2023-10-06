# Defining the ChessBoard class
class ChessBoard:
    def __init__(self):
        # Prompting the user to enter the board size
        while True:
            self.SizeBoard = int(input("Enter Board Size that greater than 3: "))
            if self.SizeBoard>3:
                break
        # Initializing the board with empty spaces
        self.Board = [[' ']*self.SizeBoard for row in range(self.SizeBoard)]
    
    def ValidValue(self,X,Y):
        # Checking if there is already a queen in the same row
        if self.Board[X-1].count('Q')>0:
            return False
        # Checking if there is already a queen in the same column
        for IndexRow in range(self.SizeBoard-1,-1,-1):
            if self.Board[IndexRow][Y-1]=='Q':
                return False
        # Checking if there is already a queen in the same diagonal (bottom-right to top-left)
        SheftDiagRL = min(self.SizeBoard-X,self.SizeBoard-Y)
        startDiagRL = [X+SheftDiagRL,Y+SheftDiagRL]
        x,y = startDiagRL[0],startDiagRL[1]
        while x>0 and y>0:
            if self.Board[x-1][y-1]=='Q':
                return False
            x-=1
            y-=1

        # Checking if there is already a queen in the same diagonal (left-bottom to top-right)
        SheftDiagLR = min(self.SizeBoard-X,Y-1)
        startDiagLR = [SheftDiagLR+X,Y-SheftDiagLR]
        x,y = startDiagLR[0],startDiagLR[1]
        while x>0 and y<=self.SizeBoard:
            if self.Board[x-1][y-1]=='Q':
                return False
            x-=1
            y+=1
        return True

    # Checking if the given position is valid and does not violate any rules
    def UpdateBoard(self,X,Y):
        if X>0 and X<=self.SizeBoard and Y>0 and Y<=self.SizeBoard and self.ValidValue(X,Y):
            # Placing the queen on the board
            self.Board[X-1][Y-1]='Q'
            return True
        return False
    
    # Printing the current state of the board
    def PrintBoard(self):
        print()
        print("--------"*self.SizeBoard+"-"*(1+self.SizeBoard))
        for i in range(self.SizeBoard):
            print("| ",end="")
            for j in range(self.SizeBoard):
                print(f"   {self.Board[i][j]}  " if self.Board[i][j]!=' ' else f"{i+1,j+1}",end = ' | ')
            print()
            print("--------"*self.SizeBoard+"-"*(1+self.SizeBoard))
        print()
    
    # Checking if all queens have been placed on the board without violating any rules
    def IsWinner(self):
        NumQueens=0
        for row in self.Board:
            NumQueens+=row.count('Q')
        return NumQueens==self.SizeBoard

