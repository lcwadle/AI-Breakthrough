class Player:
    def __init__(self, symbol):
        if symbol == 'x':
            self.direction = 1
        elif symbol == 'o':
            self.direction = -1
        else:
            print("Invalid starting symbol")
        self.symbol = symbol

    def moveStraight(self, row, col, board):
        if self.symbol == 'x':
            if board[row + self.direction][col] == '-' and board[row][col] == 'x':
                board[row + self.direction][col] = 'x'
                board[row][col] = '-'
        if self.symbol == 'o':
            if board[row + self.direction][col] == '-' and board[row][col] == 'o':
                board[row + self.direction][col] = 'o'
                board[row][col] = '-'
        return board

    def moveLeft(self, row, col, board):
        if self.symbol == 'x':
            if board[row + self.direction][col + self.direction] == '-' and board[row][col] == 'x':
                board[row + self.direction][col + self.direction] = 'x'
                board[row][col] = '-'
        if self.symbol == 'o':
            if board[row + self.direction][col + self.direction] == '-' and board[row][col] == 'o':
                board[row + self.direction][col + self.direction] = 'o'
                board[row][col] = '-'
        return board

    def moveRight(self, row, col, board):
        if self.symbol == 'x':
            if board[row + self.direction][col - self.direction] == '-' and board[row][col] == 'x':
                board[row + self.direction][col - self.direction] = 'x'
                board[row][col] = '-'
        if self.symbol == 'o':
            if board[row + self.direction][col - self.direction] == '-' and board[row][col] == 'o':
                board[row + self.direction][col - self.direction] = 'o'
                board[row][col] = '-'
        return board

class Board:
    def __init__(self, rows, cols):
        self.board = []
        for i in range(0, rows):
            row = []
            for j in range(0, cols):
                if i < 2:
                    row.append('x')
                elif i > rows - 3:
                    row.append('o')
                else:
                    row.append('-')
            self.board.append(row)

    def printBoard(self):
        border = "="
        for i in range(len(self.board[0]) + 1):
            border += '='
        print(border)
        for row in self.board:
            line = '|'
            for char in row:
                line += char
            line += '|'
            print(line)
        print(border)
