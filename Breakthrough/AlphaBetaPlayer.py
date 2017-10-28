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
        temp_active_distance = state.active_player.shortest_distance
        temp_inactive_distance = state.inactive_player.shortest_distance
        alpha = float("-inf")
        beta = float("inf")
        for move in moves:
            #print(move.newPosition)
            self.moves_expanded += 1
            value = self.min_value(state.move(move) , alpha, beta, depth)
            print(value)
            alpha = max(alpha, value)
            if value > best_score:
                best_score = value
                best_move = move
            state.active_player.pieces = temp_active_pieces
            state.inactive_player.pieces = temp_inactive_pieces
            state.active_player.shortest_distance = temp_active_distance
            state.inactive_player.shortest_distance = temp_inactive_distance

        if best_score == float("-inf"):
            best_move = moves[0]
        print(self.moves_expanded)
        print(best_score)
        return best_move

    def min_value(self, state, alpha, beta, depth):
        depth -= 1

        if state.goal:
            return 100 + (100 * depth)
        if depth == 0:
            return state.inactive_player.heuristic(state, state.active_player, state.inactive_player)

        value = float("inf")
        temp_active_pieces = state.active_player.pieces
        temp_inactive_pieces = state.inactive_player.pieces
        temp_active_distance = state.active_player.shortest_distance
        temp_inactive_distance = state.inactive_player.shortest_distance
        for move in state.get_moves():
            self.moves_expanded += 1
            value = min(value, self.max_value(state.move(move), alpha, beta, depth))
            if value <= alpha:
                return value
            beta = min(beta, value)
            state.active_player.pieces = temp_active_pieces
            state.inactive_player.pieces = temp_inactive_pieces
            state.active_player.shortest_distance = temp_active_distance
            state.inactive_player.shortest_distance = temp_inactive_distance
        return value

    def max_value(self, state, alpha, beta, depth):
        depth -= 1
        if state.goal:
            return -100 - (100 * depth)

        if depth == 0:
            return state.active_player.heuristic(state, state.inactive_player, state.active_player)

        value = float("-inf")
        temp_active_pieces = state.active_player.pieces
        temp_inactive_pieces = state.inactive_player.pieces
        temp_active_distance = state.active_player.shortest_distance
        temp_inactive_distance = state.inactive_player.shortest_distance
        for move in state.get_moves():
            self.moves_expanded += 1
            value = max(value, self.min_value(state.move(move), alpha, beta, depth))
            if value >= beta:
                return value
            alpha = max(alpha, value)
            state.active_player.pieces = temp_active_pieces
            state.inactive_player.pieces = temp_inactive_pieces
            state.active_player.shortest_distance = temp_active_distance
            state.inactive_player.shortest_distance = temp_inactive_distance
        return value
