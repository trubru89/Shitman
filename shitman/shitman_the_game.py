from shitman.gameboard import GameBoard
from itertools import cycle
import sys

# TO DO
# player can play mutliple cards if same (only from hand)
# Player cannot finnish on 2 or 10 or ace
# if cards are played so that top 4 cards in card pile is same value  ard pile is discarded and player goes again


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


def game_rules(player, board):
    if player.is_real_player:
        card_to_play = player_plays_card(player, board)
        play_card(card_to_play, board, player)


def play_card(card_to_play, board, player):
    if card_to_play.rank == "ten":
        board.add_to_card_pile(card_to_play)
        board.discard_card_pile()
        board.player_draw_card(player)
        game_rules(player, board)
    elif card_to_play.rank == "two":
        board.add_to_card_pile(card_to_play)
        board.player_draw_card(player)
        game_rules(player, board)
    elif card_to_play.value >= board.top_card_in_card_pile().value:
        board.add_to_card_pile(card_to_play)
        board.player_draw_card(player)
    else:
        board.add_to_card_pile(card_to_play)
        for card in board.get_card_pile():
            player.add_card_to_hand(card)


def player_plays_card(player, board):
    if player.player_is_out_of_cards():
        print(player.get_player_name() + " Won!")
        sys.exit(0)
    else:
        return player_select_card_pile(player, board)


def player_select_card_pile(player, board):
    if not player.card_hand_is_depleted():
        return select_card_from_hand(player, board)
    elif not player.turn_up_is_depleted():
        return select_card_from_turn_up(player, board)
    elif not player.turn_down_is_depleted:
        return select_card_from_turn_down(player, board)


def select_card_from_hand(player, board):
    current_player_hand = player.show_card_hand()
    print(player.player_name)
    print("Card on the board is: " + board.top_card_in_card_pile().suit + " " + board.top_card_in_card_pile().rank)
    for card in current_player_hand:
        print(card.get_suit() + " " + card.get_rank())
    while True:
        card_index = int(input("Select card to play (1,2,3..): "))
        if 0 < card_index <= len(current_player_hand):
            break
    return player.draw_card_from_hand(card_index-1)


def select_card_from_turn_up(player, board):
    current_player_turn_up = player.show_turn_up()
    print(player.player_name)
    print("Card on the board is: " + board.top_card_in_card_pile().suit + " " + board.top_card_in_card_pile().rank)
    for card in current_player_turn_up:
        print(card.get_suit() + " " + card.get_rank())
    while True:
        card_index = int(input("select card to play (1,2,3 ..): "))
        if 0 < card_index <= len(current_player_turn_up):
            break
    return player.draw_card_from_turn_up(card_index-1)


def select_card_from_turn_down(player, board):
    current_player_turn_down = player.show_turn_down()
    print(player.player_name)
    print("Card on the board is: " + board.top_card_in_card_pile().suit + " " + board.top_card_in_card_pile().rank)
    while True:
        card_index = int(input("Select a card, you have {} left".format(len(current_player_turn_down))))
        if 0 < card_index <= len(current_player_turn_down):
            break
    return player.draw_card_from_turn_down(card_index-1)


def main():
    board, players = init_a_game()
    players = who_goes_first(players)
    player_cycle = cycle(players)
    player = next(player_cycle)
    while True:
        game_rules(player, board)
        player = next(player_cycle)


if __name__ == "__main__":
    main()
