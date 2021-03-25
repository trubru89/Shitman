from shitman import gameboard
from itertools import cycle


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


def player_action(player):
    pass


def main():
    board, players = init_a_game()
    players = who_goes_first(players)
    player_action(players[0])  # First player turn
    pool = cycle(players)  # To iterate over players
    # loop here
    player_action(player_turn_iterator(pool))


if __name__ == "__main__":
    main()
