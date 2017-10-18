class Player:
    def __init__(self, symbol):
        self.symbol = symbol

        if symbol == 'o':
            self.direction = -1
        if symbol == 'x':
            self.direction = 1
