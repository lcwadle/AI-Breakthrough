from copy import deepcopy

class MinimaxPlayer:
    def __init__(self, state, depth):
        self.depth = depth

    def get_move(self, state):
        return self.minimax(state, self.depth)

    def minimax(self, state, depth):
        self.moves_expanded = 0
        best_score = float("-inf")
        best_move = None
        moves = state.get_moves()
        for move in moves:
            self.moves_expanded += 1
            value = self.min_value(state.move(move), depth)
            if value > best_score:
                best_score = value
                best_move = move
        #print(self.moves_expanded)
        #print(best_score)
        if best_score == float("-inf"):
            best_move = moves[0]
        state.active_player.nodes_expanded += self.moves_expanded
        return best_move

    def min_value(self, state, depth):
        depth -= 1

        if state.goal:
            return 100 + (100 * depth)
        if depth == 0:
            return state.inactive_player.heuristic(state, state.active_player, state.inactive_player)

        value = float("inf")
        for move in state.get_moves():
            self.moves_expanded += 1
            value = min(value, self.max_value(state.move(move), depth))
        return value

    def max_value(self, state, depth):
        depth -= 1

        if state.goal:
            return float("-inf")

        if depth == 0:
            return state.active_player.heuristic(state, state.inactive_player, state.active_player)

        value = float("-inf")
        for move in state.get_moves():
            self.moves_expanded += 1
            value = max(value, self.min_value(state.move(move), depth))
        return value
