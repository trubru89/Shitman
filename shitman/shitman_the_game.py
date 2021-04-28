from shitman.gameboard import GameBoard
from itertools import cycle
import sys


special_cards = [2, 10]


def init_a_game():
    board = GameBoard()
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
    cards = [player.get_lowest_card_in_hand() for player in players]
    if cards.index(min(cards)) != 0:
        players[cards.index(min(cards))], players[0] = players[0], players[cards.index(min(cards))]
    return players


def player_turn_iterator(pool):
    player = next(pool)
    return player


def player_action(player, board):
    if player.is_real_player():
        top_card = board.top_card_in_card_pile()
        player_card = player.select_where_to_draw_card(top_card)
        if not player_card:
            return player.player_name
        elif player_card.value in special_cards:
            if player_card.value == 2:
                board.add_to_card_pile(player_card)
                if board.game_deck_is_not_depleted():
                    player.add_card(board.draw_from_game_deck())
                # player goes again
            elif player_card.value == 10:
                board.add_to_card_pile(player_card)
                board.card_pile.discard_card_pile()
                if board.game_deck_is_not_depleted():
                    player.add_card(board.draw_from_game_deck())
                # player goes again
        elif player_card.value < top_card.value:
            print("Player cannot put card {} {} over {} {}".format(player_card.suit, player_card.value,
                                                                   top_card.suit, top_card.value))
            player.add_card(player_card)
            for a_card in board.card_pile.throw_card_pile():
                player.add_card(a_card)
        else:
            print("Can play card")
            board.add_to_card_pile(player_card)
            if board.game_deck_is_not_depleted():
                print("Game deck is not depleted")
                player.add_card(board.draw_from_game_deck())
            else:
                print("Game deck is depleted")


def main():
    board, players = init_a_game()
    players = who_goes_first(players)
    player_action(players[0], board)  # First player turn
    # loop here
    pool = cycle(players)  # To iterate over players
    player_action(player_turn_iterator(pool), board)


if __name__ == "__main__":
    main()
