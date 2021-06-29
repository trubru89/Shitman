import random
from shitman.card import Card


class CardDeck:

    def __init__(self):
        self.suits = ["Heart", "Spade", "Clove", "Diamond"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.ranks = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack",
                     "queen", "king", "ace"]
        self.deck = []
        self.drawn_card = None

    def compile_deck(self):
        self.deck = [Card(suit, value, rank) for suit in self.suits for value, rank in zip(self.values, self.ranks)]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_from_deck(self):
        if self.deck:
            drawn_card = self.deck.pop(0)
            return drawn_card
        return False

    def get_deck(self):
        return [a_card for a_card in self.deck]

    def show_deck(self):
        print(self.deck)

#    def draw_random_card(self):
#        return random.choice(self.deck)

    def deck_is_not_depleted(self):
        return self.deck
