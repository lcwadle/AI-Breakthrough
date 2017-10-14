import Breakthrough

board = Breakthrough.Board(8, 8)
board.printBoard()
player1 = Breakthrough.Player('x')
player2 = Breakthrough.Player('o')

count = 0
while count < 10:
    if count % 2 == 0:
        print("Player 'o' Turn")
        piece = input("What piece would you like to move (x,y): ")
        x, y = piece.split(',')
        board.board = player2.moveStraight(int(x), int(y), board.board)
    else:
        print("Player 'x' Turn")
        piece = input("What piece would you like to move (x,y): ")
        x, y = piece.split(',')
        board.board = player1.moveStraight(int(x), int(y), board.board)
    board.printBoard()
    count += 1
