import unittest
from shitman import carddeck


def test_card_deck_size():
    cd = carddeck.CardDeck()
    cd.compile_deck()
    assert len(cd.get_deck()) == 52, "Created deck does not have 52 cards"


def test_draw_whole_deck():
    cd = carddeck.CardDeck()
    cd.compile_deck()
    for card in range(len(cd.get_deck())):
        draw_card = cd.draw_from_deck()
    assert cd.draw_from_deck() is False


def test_shuffle_deck():
    cd = carddeck.CardDeck()
    cd.compile_deck()
    cd.shuffle_deck()
    card_from_shuffled = cd.draw_from_deck()


