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
                        if self.board.board[piece.row + direction][piece.col + direction].value != '-':
                            moves.insert(0,Move.Move((piece.row, piece.col), (piece.row + direction, piece.col + direction)))
                        else:
                            moves.append(Move.Move((piece.row, piece.col), (piece.row + direction, piece.col + direction)))
            # Right
            if piece.row + direction >= 0 and piece.row + direction < self.board.rows:
                if piece.col - direction >= 0 and piece.col - direction < self.board.cols:
                    if self.board.board[piece.row + direction][piece.col - direction].value != self.active_player.symbol:
                        if self.board.board[piece.row + direction][piece.col - direction].value != '-':
                            moves.insert(0,Move.Move((piece.row, piece.col), (piece.row + direction, piece.col - direction)))
                        else:
                            moves.append(Move.Move((piece.row, piece.col), (piece.row + direction, piece.col - direction)))

        #for move in moves:
            #print(str(move.currentPosition[0]) + ',' + str(move.currentPosition[1]) + " to " + str(move.newPosition[0]) + ',' + str(move.newPosition[1]))

        return moves

    def move(self, move):
        new_board = deepcopy(self.board)
        new_board.board[move.currentPosition[0]][move.currentPosition[1]].value = '-'
        if new_board.board[move.newPosition[0]][move.newPosition[1]].value != '-':
            self.inactive_player.pieces -= 1
        new_board.board[move.newPosition[0]][move.newPosition[1]].value = self.active_player.symbol
        new_state = State(new_board, self.inactive_player, self.active_player)


        if self.active_player.symbol == 'o' and move.newPosition[0] < self.active_player.shortest_distance:
            self.active_player.shortest_distance = move.newPosition[0]
            #print(self.active_player.shortest_distance)
        if self.active_player.symbol == 'x' and 7 - move.newPosition[0] < self.active_player.shortest_distance:
            self.active_player.shortest_distance = 7 - move.newPosition[0]
            #print(self.active_player.shortest_distance)

        if move.newPosition[0] == 0 or new_state.active_player.pieces == 0:
            new_state.goal = True
        if move.newPosition[0] == new_state.board.rows - 1 or new_state.active_player.pieces == 0:
            new_state.goal = True
        return new_state
