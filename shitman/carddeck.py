import random
from shitman import card


class CardDeck:

    def __init__(self):
        self.suits = ["Heart", "Spade", "Clove", "Diamond"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.deck = []
        self.drawn_card = None

    def compile_deck(self):
        self.deck = [card.Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_from_deck(self):
        if self.deck:
            drawn_card = self.deck.pop(0)
            return drawn_card
        else:
            return False

    def get_deck(self):
        return [a_card for a_card in self.deck]

    def show_deck(self):
        print(self.deck)

#    def draw_random_card(self):
#        return random.choice(self.deck)

    def deck_is_depleted(self):
        return False if self.deck else True
