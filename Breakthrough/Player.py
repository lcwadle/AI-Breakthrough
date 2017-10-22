import random

class Player:
    def __init__(self, symbol, heuristic):
        self.symbol = symbol
        self.pieces = 16
        self.captures = 0
        if heuristic == "offense_1":
            self.heuristic = self.offense_1
        if heuristic == "defense_1":
            self.heuristic = self.defense_1

        if symbol == 'o':
            self.direction = -1
        if symbol == 'x':
            self.direction = 1

    def defense_1(self, state):
        # Number of pieces remaining for active_player
        return 2 * state.active_player.pieces + random.random()

    def offense_1(self, state):
        # Number of pieces remaining for active_player

        return 2 * (30 - state.inactive_player.pieces) + random.random()
