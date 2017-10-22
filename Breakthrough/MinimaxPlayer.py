from copy import deepcopy

class MinimaxPlayer:
    def __init__(self, state, depth):
        self.depth = depth

    def get_move(self, state):
        return self.minimax(state, self.depth)

    def minimax(self, state, depth):
        best_score = float("-inf")
        best_move = None
        moves = state.get_moves()
        temp_active_pieces = state.active_player.pieces
        temp_inactive_pieces = state.inactive_player.pieces
        for move in moves:
            value = self.min_value(state, depth)
            if value > best_score:
                best_score = value
                best_move = move
        state.active_player.pieces = temp_active_pieces
        state.inactive_player.pieces = temp_inactive_pieces
        return best_move

    def min_value(self, state, depth):
        depth -= 1

        if state.goal:
            return 1
        if depth == 0:
            return state.active_player.heuristic(state)

        value = float("inf")
        for move in state.get_moves():
            value = min(value, self.max_value(state.forecast_move(move), depth))
        return value

    def max_value(self, state, depth):
        depth -= 1
        if state.goal:
            return -1

        if depth == 0:
            return state.inactive_player.heuristic(state)

        value = float("-inf")
        for move in state.get_moves():
            value = max(value, self.max_value(state.forecast_move(move), depth))
        return value

    def heuristic(self, state, player):
        # Number of pieces remaining for active_player

        return 2 * player.pieces + random.random()
