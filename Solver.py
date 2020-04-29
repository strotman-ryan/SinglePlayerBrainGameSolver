from TurtleGameState import TurtleGameState





def Search(gameState, depth):
    if gameState.IsWinner():
        gameState.PrintState()
        return True
    if depth == 1:
        return False
    for next_state in gameState.GetNextStates():
        if Search(next_state, depth -1):
            gameState.PrintState()
            return True
    return False




if __name__ == "__main__":
    depth = 1
    board = [[1,-1,-1,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
    begin_state = TurtleGameState(board)
    while not Search(begin_state, depth):
        depth += 1
        print("--------" + str(depth) + "--------------")
