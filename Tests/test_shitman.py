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
    new_deck_values = []
    shuffled_values = []
    cd = carddeck.CardDeck()
    cd.compile_deck()
    new_deck = cd.get_deck()
    cd.shuffle_deck()
    shuffled_deck = cd.get_deck()
    for new_deck_card in new_deck:
        new_deck_values.append(new_deck_card.value)
    for shuffled_card in shuffled_deck:
        shuffled_values.append(shuffled_card.value)
    assert new_deck_values != shuffled_values


# Card test
def test_card():
    one_card = card.Card("Heart", 2)
    assert one_card.get_suit() == "Heart"
    assert one_card.get_value() == 2


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


# Cardhand tests.
# Create player hand
# Add a card
# Get smallest card value from hand
# Remove a card until hand is empty
def test_start_hand():
    suits = ["Heart", "Spade", "Clove", "Diamond"]
    values = [2, 3, 4]
    card_one = card.Card("Heart", 2)
    card_two = card.Card("Spade", 4)
    card_three = card.Card("Clove", 7)
    player_hand = [card_one, card_two, card_three]
    ch = cardhand.CardHand()
    ch.get_start_hand(player_hand)
    assert ch.number_of_cards_in_hand() == 3
    ch.add_card(card.Card("Heart", 5))
    assert ch.number_of_cards_in_hand() == 4
    assert ch.show_lowest_card_in_hand() == card_one.value
    ch.remove_card(card.Card("Heart", 5))
    assert ch.number_of_cards_in_hand() == 3
    ch.remove_card(card_three)
    assert ch.number_of_cards_in_hand() == 2
    assert ch.remove_card(card_two) == card_two
    assert ch.number_of_cards_in_hand() == 1
    ch.remove_card(card_one)
    assert ch.number_of_cards_in_hand() is False

