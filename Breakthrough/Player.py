import random

class Player:
    def __init__(self, symbol, heuristic):
        self.symbol = symbol
        self.pieces = 16
        self.shortest_distance = 7

        if heuristic == "offense_1":
            self.heuristic = self.offense_1
        if heuristic == "defense_1":
            self.heuristic = self.defense_1
        if heuristic == "offense_2":
            self.heuristic = self.offense_2
        if heuristic == "defense_2":
            self.heuristic = self.defense_2

        if symbol == 'o':
            self.direction = -1
        if symbol == 'x':
            self.direction = 1

    def defense_1(self, state, player, inactive_player):
        # Number of pieces remaining for active_player
        return 2 * player.pieces + random.random()

    def offense_1(self, state, player, inactive_player):
        # Number of pieces remaining for the inactive_player
        return 2 * (30 - player.pieces) + random.random()

    def offense_2(self, state, player, inactive_player):
        # Number of pieces remaining for the inactive player and minimize the shortest distance to goal for active_player
        return 2 * (30 - player.pieces) - 2 * (30 - inactive_player.pieces) - 2 * player.shortest_distance + random.random()

    def defense_2(self, state, player, inactive_player):
        # Number of pieces remaining for the active_player and maximize the shortest distance to goal for inactive_player
        return 2 * player.pieces + random.random() + inactive_player.shortest_distance
