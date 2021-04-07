from shitman import gameboard
from itertools import cycle


game_dict = {
    "card_deck_empty": "",
    "player_hand_empty": "",
    "player_cannot_play_card": "",
    "player_turn_up_is_depleted": "",
    "player_turn_down_is_depleted": ""
}


def init_a_game():
    board = gameboard.GameBoard()
    board.shuffle_board_deck()
    players = board.set_up_players()
    for player in players:
        player.get_start_hand(board.get_player_start_hand())
        player.get_player_turn_down(board.get_player_turndown())
        player.get_player_turn_up(board.get_player_turnup())
    return board, players


# Only checks who has the lowest card value and does not care about suites
# So if two or more players has same value basically random goes first
def who_goes_first(players):
    cards = [player.show_lowest_card_in_hand() for player in players]
    if cards.index(min(cards)) != 0:
        players[cards.index(min(cards))], players[0] = players[0], players[cards.index(min(cards))]
    return players


def player_turn_iterator(pool):
    player = next(pool)
    return player


# crap... rethink
def player_action(player, board):
    if board.game_deck_is_depleted():
        if player.select_where_to_draw_card() is True:
            print("Player: " + player + " has won!")
    else:
        pass

    if player.is_real_player:
        pass


def main():
    board, players = init_a_game()
    players = who_goes_first(players)
    player_action(players[0], board)  # First player turn
    # loop here
    pool = cycle(players)  # To iterate over players
    player_action(player_turn_iterator(pool), board)


if __name__ == "__main__":
    main()
