import unittest
from shitman import carddeck
from shitman import card
from shitman import gameboard


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
    cd.shuffle_deck()
    card_from_shuffled = cd.draw_from_deck()


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
    assert len(gameboard_two.get_player_start_hand()) == 3


