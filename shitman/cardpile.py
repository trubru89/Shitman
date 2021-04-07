

class CardPile:

    def __init__(self):
        self.card_pile = []
        self.discard_pile = []

    def add_to_card_pile(self, card):
        self.card_pile.insert(0, card)

    def throw_card_pile(self):
        self.discard_pile.append(self.card_pile)
        self.card_pile = []

    def show_top_card_in_card_pile(self):
        return self.card_pile[0] if self.card_pile else False
