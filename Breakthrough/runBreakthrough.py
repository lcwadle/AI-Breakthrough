import Board
import Player
import State
import MinimaxPlayer
import AlphaBetaPlayer
from timeit import default_timer as timer

start = timer()
num_moves = 0

board = Board.Board(8, 8)
player_1 = Player.Player('o', "offense_1")
player_2 = Player.Player('x', "offense_2")

state = State.State(board, player_1, player_2)
state.board.print_board()
print("Begin...")
i = 0
while not state.goal:
    if i % 2 == 1:
        player1 = player_2
        player2 = player_1
        player = AlphaBetaPlayer.AlphaBetaPlayer(state, 3)
    else:
        player1 = player_1
        player2 = player_2
        player = AlphaBetaPlayer.AlphaBetaPlayer(state, 3)

    move = player.get_move(state)
    print("Player " + state.active_player.symbol)
    state = state.move(move)
    state.board.print_board()
    print("Player " + state.active_player.symbol + " pieces: " + str(state.active_player.pieces))
    print("Player " + state.inactive_player.symbol + " pieces: " + str(state.inactive_player.pieces))
    num_moves += 1
    i += 1

end = timer()
state.board.print_board()
print("Player " + state.inactive_player.symbol + " wins!")
print("Captures: " + str(18 - state.active_player.pieces))
print()
print(str(num_moves) + " moves with an average time of " + str((end-start) / num_moves) + ".")
