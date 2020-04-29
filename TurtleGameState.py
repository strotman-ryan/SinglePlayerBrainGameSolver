import copy

class TurtleGameState:

    def __init__(self,state_rep):
        '''
        State rep is a 4x4 matrix of python arrays
        -1 is a turtle belly up
        0 is an empty space
        1 is a turtle back up
        '''
        self.state_rep = state_rep


    def IsWinner(self):
        '''
        IsWinner() -> (boolean)
        returns true if this game state wins
        '''
        for row in self.state_rep:
            for col in row:
                if col == -1:
                    return False
        return True

    def PrintState(self):
        '''
        PrintState()-> prints a depicton of the state
        '''
        print("--------------state------------------")
        for row in self.state_rep:
            string = ""
            for col in row:
                string += str(col)
            print(string)

    def GetNextStates(self):
        '''
        GetNextStates() -> list of TurtleGameState
        algorith: for each blank space find all pieces that can move into it
        make the move and save the board
        '''
        nextStates = []
        for row in range(len(self.state_rep)):
            for col in range(len(self.state_rep[row])):
                if self.state_rep[row][col] == 0:
                    #space is blank
                    nextStates.extend(self.getAllMovesToSpace(row,col))
        return nextStates



    def getAllMovesToSpace(self, rowIndex, colIndex):
        nextStates = []
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for direction in directions:
            row = rowIndex + direction[0]
            col = colIndex + direction[1]
            if self.inBounds(row, col):
                if self.state_rep[row][col] != 0:
                    row += direction[0]
                    col += direction[1]
                    while self.inBounds(row, col) and self.state_rep[row][col] != 0:
                        newState = copy.deepcopy(self.state_rep)
                        newState[rowIndex][colIndex] = newState[row][col]
                        newState[row][col] = 0
                        rowTemp = row - direction[0]
                        colTemp = col - direction[1]
                        while rowTemp != rowIndex or colTemp != colIndex:
                            newState[rowTemp][colTemp] *= -1
                            rowTemp -= direction[0]
                            colTemp -= direction[1]
                        nextStates.append(TurtleGameState(newState))
                        row += direction[0]
                        col += direction[1]
        return nextStates
                        


    def inBounds(self,rowIndex, colIndex):
        '''
        inBounds(int, int)->boolean
        return true if the index are not outside the game matrix
        '''
        if rowIndex < 0:
            return False
        if colIndex < 0:
            return False
        if rowIndex >= len(self.state_rep):
            return False
        if colIndex >= len(self.state_rep[0]):
            return False
        return True
