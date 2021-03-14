from shitman import gameboard


def init_a_game():
    board = gameboard.GameBoard()
    players = board.set_up_players()
    board.shuffle_board_deck()
    for player in players:
        player.get_start_hand(board.get_player_start_hand())
        player.get_player_turn_down(board.get_player_turndown())
        player.get_player_turn_up(board.get_player_turnup())


def main():
    init_a_game()


if __name__ == "__main__":
    main()
