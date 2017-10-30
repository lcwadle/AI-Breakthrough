import random

class Player:
    def __init__(self, symbol, heuristic):
        self.symbol = symbol
        self.pieces = 16
        self.shortest_distance = 7
        self.nodes_expanded = 0
        self.goal_pieces = 0

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
        #print("Player " + player.symbol)
        #state.board.print_board()
        #print("Opponent pieces: " + str(16 - player.pieces) + ", Player pieces: " + str(inactive_player.pieces) + ", Distance: " + str(inactive_player.shortest_distance))
        #input("Press enter")
        return 3 * (16 - player.pieces) + 2 * inactive_player.pieces + 2.5 * (7 - inactive_player.shortest_distance) + 2.5 * inactive_player.goal_pieces + random.random()

    def defense_2(self, state, player, inactive_player):
        # Number of pieces remaining for the active_player and maximize the shortest distance to goal for inactive_player
        return 3 * inactive_player.pieces + 2 * player.shortest_distance + 2 * (7 - inactive_player.shortest_distance) + 2.5 * inactive_player.goal_pieces + random.random()
