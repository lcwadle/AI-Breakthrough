from copy import deepcopy

class AlphaBetaPlayer:
    def __init__(self, state, depth):
        self.depth = depth

    def get_move(self, state):
        return self.alpha_beta(state, self.depth)

    def alpha_beta(self, state, depth):
        self.moves_expanded = 0
        best_score = float("-inf")
        best_move = None
        moves = state.get_moves()
        temp_active_pieces = state.active_player.pieces
        temp_inactive_pieces = state.inactive_player.pieces
        alpha = float("-inf")
        beta = float("inf")
        for move in moves:
            print(move.newPosition)
            state.active_player.pieces = temp_active_pieces
            state.inactive_player.pieces = temp_inactive_pieces
            self.moves_expanded += 1
            value = self.min_value(state.move(move) , alpha, beta, depth)
            print(value)
            alpha = max(alpha, value)
            if value > best_score:
                best_score = value
                best_move = move
        state.active_player.pieces = temp_active_pieces
        state.inactive_player.pieces = temp_inactive_pieces
        print(self.moves_expanded)
        print(best_score)
        return best_move

    def min_value(self, state, alpha, beta, depth):
        depth -= 1

        if state.goal:
            return float("inf")
        if depth == 0:
            return state.inactive_player.heuristic(state, state.active_player)

        value = float("inf")
        temp_active_pieces = state.active_player.pieces
        temp_inactive_pieces = state.inactive_player.pieces
        for move in state.get_moves():
            state.active_player.pieces = temp_active_pieces
            state.inactive_player.pieces = temp_inactive_pieces
            self.moves_expanded += 1
            value = min(value, self.max_value(state.move(move), alpha, beta, depth))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

    def max_value(self, state, alpha, beta, depth):
        depth -= 1
        if state.goal:
            return float("-inf")

        if depth == 0:
            return state.active_player.heuristic(state, state.inactive_player)

        value = float("-inf")
        temp_active_pieces = state.active_player.pieces
        temp_inactive_pieces = state.inactive_player.pieces
        for move in state.get_moves():
            state.active_player.pieces = temp_active_pieces
            state.inactive_player.pieces = temp_inactive_pieces
            self.moves_expanded += 1
            value = max(value, self.min_value(state.move(move), alpha, beta, depth))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value
