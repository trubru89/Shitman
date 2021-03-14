from shitman import gameboard

# stage1 = game deck is not depleted. player1 can be in stage1 while player2 is in stage2
# fill with functions

game_dict = {
  "stage1": "",
  "stage2": "",

}


def init_a_game():
    board = gameboard.GameBoard()
    board.shuffle_board_deck()
    players = board.set_up_players()
    for player in players:
        player.get_start_hand(board.get_player_start_hand())
        player.get_player_turn_down(board.get_player_turndown())
        player.get_player_turn_up(board.get_player_turnup())


def main():
    init_a_game()


if __name__ == "__main__":
    main()
