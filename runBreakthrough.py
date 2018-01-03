import Board
import Player
import State
import MinimaxPlayer
import AlphaBetaPlayer
import HumanPlayer
from timeit import default_timer as timer
for j in range(0, 10):
    start = timer()
    num_moves = 0

    board = Board.Board(8, 8)
    player_1 = Player.Player('o', "offense_2")
    player_2 = Player.Player('x', "defense_1")

    state = State.State(board, player_1, player_2)
    state.board.print_board()
    #print("Begin...")
    i = 0
    while not state.goal:
        if i % 2 == 1:
            player = AlphaBetaPlayer.AlphaBetaPlayer(state, 4)
        else:
            player = HumanPlayer.HumanPlayer(state)

        move = player.get_move(state)
        if move == None:
            break
        #print("Player " + state.active_player.symbol)
        state = state.move(move)
        state.board.print_board()
        #print("Player " + state.active_player.symbol + " pieces: " + str(state.active_player.pieces))
        #print("Player " + state.inactive_player.symbol + " pieces: " + str(state.inactive_player.pieces))
        #print("Player " + state.active_player.symbol + " distance: " + str(state.active_player.shortest_distance))
        #print("Player " + state.inactive_player.symbol + " distance: " + str(state.inactive_player.shortest_distance))
        num_moves += 1
        i += 1

    end = timer()
    state.board.print_board()
    print("Player " + state.inactive_player.symbol + " wins!")
    print("Captures: " + str(18 - state.active_player.pieces))
    print()
    print("Player " + state.inactive_player.symbol + " Tree Nodes Expanded: " + str(state.inactive_player.nodes_expanded))
    print("Player " + state.active_player.symbol + " Tree Nodes Expanded: " + str(state.active_player.nodes_expanded))
    print(str(num_moves) + " moves with an average time of " + str((end-start) / num_moves) + ".")
    print("Average nodes expanded per move: " + str((state.active_player.nodes_expanded + state.inactive_player.nodes_expanded) / float(num_moves)))
