import Move

class State:
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def getPieces(self):
        pieces = []

        # Find all available moves
        for row in self.board.board:
            for node in row:
                if node.value == self.player.symbol:
                    pieces.append(node)

        return pieces

    def getMoves(self):
        moves = []
        direction = self.player.direction

        pieces = self.getPieces()
        for piece in pieces:
            #print(str(piece.row) + ',' + str(piece.col))
            # Straight
            if piece.row + direction >= 0 and piece.row + direction < self.board.rows:
                if self.board.board[piece.row + direction][piece.col].value == '-':
                    moves.append(Move.Move((piece.row, piece.col), (piece.row + direction, piece.col)))
            # Left
            if piece.row + direction >= 0 and piece.row + direction < self.board.rows:
                if piece.col + direction >= 0 and piece.col + direction < self.board.cols:
                    if self.board.board[piece.row + direction][piece.col + direction].value != self.player.symbol:
                        moves.append(Move.Move((piece.row, piece.col), (piece.row + direction, piece.col + direction)))
            # Right
            if piece.row + direction >= 0 and piece.row + direction < self.board.rows:
                if piece.col - direction >= 0 and piece.col - direction < self.board.cols:
                    if self.board.board[piece.row + direction][piece.col - direction].value != self.player.symbol:
                        moves.append(Move.Move((piece.row, piece.col), (piece.row + direction, piece.col - direction)))

        #for move in moves:
            #print(str(move.currentPosition[0]) + ',' + str(move.currentPosition[1]) + " to " + str(move.newPosition[0]) + ',' + str(move.newPosition[1]))

        return moves
