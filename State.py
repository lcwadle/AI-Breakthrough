import Move
from copy import deepcopy

class State:
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.active_player = player_1
        self.inactive_player = player_2
        self.goal = False

    def get_pieces(self, player):
        pieces = []

        # Find all available moves
        for row in self.board.board:
            for node in row:
                if node.value == player.symbol:
                    pieces.append(node)

        return pieces

    def get_moves(self):
        moves = []
        direction = self.active_player.direction

        pieces = self.get_pieces(self.active_player)
        for piece in pieces:
            #print(str(piece.row) + ',' + str(piece.col))
            # Straight
            if piece.row + direction >= 0 and piece.row + direction < self.board.rows:
                if self.board.board[piece.row + direction][piece.col].value == '-':
                    moves.append(Move.Move((piece.row, piece.col), (piece.row + direction, piece.col)))
            # Left
            if piece.row + direction >= 0 and piece.row + direction < self.board.rows:
                if piece.col + direction >= 0 and piece.col + direction < self.board.cols:
                    if self.board.board[piece.row + direction][piece.col + direction].value != self.active_player.symbol:
                        moves.append(Move.Move((piece.row, piece.col), (piece.row + direction, piece.col + direction)))
            # Right
            if piece.row + direction >= 0 and piece.row + direction < self.board.rows:
                if piece.col - direction >= 0 and piece.col - direction < self.board.cols:
                    if self.board.board[piece.row + direction][piece.col - direction].value != self.active_player.symbol:
                        moves.append(Move.Move((piece.row, piece.col), (piece.row + direction, piece.col - direction)))

        sorted_moves = []
        for move in moves:
            if self.board.board[move.newPosition[0]][move.newPosition[1]].value != '-':
                sorted_moves.insert(0, move)
            elif self.active_player.symbol == 'o' and move.newPosition[0] < self.active_player.shortest_distance:
                sorted_moves.insert(0, move)
            elif self.active_player.symbol == 'x' and (7 - move.newPosition[0]) < self.active_player.shortest_distance:
                sorted_moves.insert(0, move)
            else:
                sorted_moves.append(move)

        #for move in moves:
            #print(str(move.currentPosition[0]) + ',' + str(move.currentPosition[1]) + " to " + str(move.newPosition[0]) + ',' + str(move.newPosition[1]))

        return sorted_moves

    def move(self, move):
        new_board = deepcopy(self.board)
        new_board.board[move.currentPosition[0]][move.currentPosition[1]].value = '-'
        new_board.board[move.newPosition[0]][move.newPosition[1]].value = self.active_player.symbol

        new_state = State(new_board, self.inactive_player, self.active_player)
        min_distance = 7
        pieces = new_state.get_pieces(new_state.inactive_player)
        new_state.inactive_player.goal_pieces = 0
        for piece in pieces:
            if new_state.inactive_player.symbol == 'o':
                if piece.row == 0:
                    new_state.inactive_player.goal_pieces += 1
                min_distance = min(piece.row, min_distance)
            if new_state.inactive_player.symbol == 'x':
                if piece.row == new_state.board.rows - 1:
                    new_state.inactive_player.goal_pieces += 1
                min_distance = min(7 - piece.row, min_distance)
        new_state.inactive_player.shortest_distance = min_distance
        new_state.inactive_player.pieces = len(pieces)
        min_distance = 7
        pieces = new_state.get_pieces(new_state.active_player)
        new_state.active_player.goal_pieces = 0
        for piece in pieces:
            if new_state.active_player.symbol == 'o':
                if piece.row == 0:
                    new_state.active_player.goal_pieces += 1
                min_distance = min(piece.row, min_distance)
            if new_state.active_player.symbol == 'x':
                if piece.row == new_state.board.rows - 1:
                    new_state.active_player.goal_pieces += 1
                min_distance = min(7 - piece.row, min_distance)
        new_state.active_player.shortest_distance = min_distance
        new_state.active_player.pieces = len(pieces)

        if new_state.inactive_player.goal_pieces == 3 or new_state.active_player.pieces == 2:
            new_state.goal = True
        return new_state
