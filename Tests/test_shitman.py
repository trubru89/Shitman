import unittest
from shitman import carddeck
from shitman import card
from shitman import gameboard
from shitman import cardhand


# Card deck tests
def test_card_deck_size():
    cd = carddeck.CardDeck()
    cd.compile_deck()
    assert len(cd.get_deck()) == 52, "Created deck does not have 52 cards"


def test_draw_whole_deck():
    cd = carddeck.CardDeck()
    cd.compile_deck()
    for a_card in range(len(cd.get_deck())):
        draw_card = cd.draw_from_deck()
    assert cd.draw_from_deck() is False


def test_shuffle_deck():
    cd = carddeck.CardDeck()
    cd.compile_deck()
    new_deck = cd.get_deck()
    cd.shuffle_deck()
    shuffled_deck = cd.get_deck()
    assert new_deck != shuffled_deck


# Card test
def test_card():
    one_card = card.Card("Heart", 2, "two")
    assert one_card.get_suit() == "Heart"
    assert one_card.get_value() == 2
    assert one_card.get_rank() == "two"


# Gameboard tests
def test_set_up_players():
    gameboard_one = gameboard.GameBoard()
    players_in_gameboard = gameboard_one.set_up_players()
    assert len(players_in_gameboard) == 2  # Default 2 players


def test_get_player_start_hand():
    gameboard_two = gameboard.GameBoard()
    player_start_hand = gameboard_two.get_player_start_hand()
    assert len(player_start_hand) == 3
    assert type(player_start_hand[0].get_suit()) is str
    assert type(player_start_hand[0].get_value()) is int
    assert type(player_start_hand[0].get_rank()) is str


def test_game_deck_draw_card():
    gameboard_three = gameboard.GameBoard()
    assert gameboard_three.game_deck_is_depleted() is False
    for game_card in range(0, 52):
        card_from_deck = gameboard_three.draw_from_game_deck()
    assert gameboard_three.draw_from_game_deck() is False
    assert gameboard_three.game_deck_is_depleted() is True


# Cardhand tests.
# Create player hand
# Add a card
# Get smallest card value from hand
# Remove a card until hand is empty
def test_start_hand():
    cd = carddeck.CardDeck()
    cd.compile_deck()
    player_hand = []
    for cards_in_start_hand in range(0, 3):
        player_hand.append(cd.draw_from_deck())
    ch = cardhand.CardHand()
    ch.get_start_hand(player_hand)
    assert ch.number_of_cards_in_hand() == 3
    ch.add_card(cd.draw_from_deck())
    assert ch.number_of_cards_in_hand() == 4
    assert ch.show_lowest_card_in_hand() == 2
    ch.remove_card(0)
    assert ch.number_of_cards_in_hand() == 3
    ch.remove_card(0)
    assert ch.number_of_cards_in_hand() == 2
    ch.remove_card(0)
    assert ch.number_of_cards_in_hand() == 1
    ch.remove_card(0)
    assert ch.number_of_cards_in_hand() == 0

