import unittest
from shitman import carddeck


def test_card_deck_size():
    cd = carddeck.CardDeck()
    cd.compile_deck()
    assert len(cd.get_deck()) == 52, "Created deck does not have 52 cards"


