import random


class CardDeck:

    def __init__(self):
        self.suits = ["H", "S", "C", "D"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck = []

    def compile_deck(self):
        self.deck = [suit + value for suit in self.suits for value in self.values]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_from_deck(self):
        if self.deck:
            drawn_card = self.deck[0]
            self.deck.pop(0)
            return drawn_card
        else:
            print("out of cards")
            return False

    def get_deck(self):
        return self.deck

    def show_deck(self):
        print(self.deck)

