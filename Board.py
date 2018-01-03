import Node

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = []

        for i in range(0, rows):
            row = []
            for j in range(0, cols):
                if i < 2:
                    node = Node.Node(i, j, 'x')
                    row.append(node)
                elif i > rows - 3:
                    node = Node.Node(i, j, 'o')
                    row.append(node)
                else:
                    node = Node.Node(i, j, '-')
                    row.append(node)
            self.board.append(row)

    def print_board(self):
        border = "="
        for i in range(len(self.board[0]) + 1):
            border += '='
        print(border)
        for row in self.board:
            line = '|'
            for node in row:
                line += node.value
            line += '|'
            print(line)
        print(border)
