import Board
import Player
import State
from copy import deepcopy

board = Board.Board(8, 8)
player_1 = Player.Player('o')
player_2 = Player.Player('x')

state = State.State(board, player_1)

for i in range (0, 10):
    player = None
    if i % 2 == 1:
        player1 = player_2
        player2 = player_1
    else:
        player1 = player_1
        player2 = player_2

    state.board.printBoard()
    newBoard = deepcopy(state.board)
    moves = state.getMoves()
    newBoard.board[moves[0].currentPosition[0]][moves[0].currentPosition[1]].value = '-'
    newBoard.board[moves[0].newPosition[0]][moves[0].newPosition[1]].value = player1.symbol
    state = State.State(newBoard, player2)
