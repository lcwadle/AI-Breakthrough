from copy import deepcopy

class HumanPlayer:
    def __init__(self, state):
        pass

    def get_move(self, state):
        print("Choose piece to move.")
        row = input("Row:")
        col = input("Column:")
        moves = state.get_moves()
        i = 0
        allowed_moves = []
        for move in moves:
            if move.currentPosition[0] == int(row) and move.currentPosition[1] == int(col):
                i += 1
                print(str(i) + ": " + str(move.newPosition[0]) + "," + str(move.newPosition[1]))
                allowed_moves.append(move)
        move = input("Move: ")
        return allowed_moves[i-1]
