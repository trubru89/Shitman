

class DiscardPile:

    def __init__(self):
        self.discard_pile = []

    def add_to_discard_pile(self, cards):
        self.discard_pile.append(cards)

    def pick_discard_pile(self):
        new_card_pile = [a_card for a_card in self.discard_pile]
        self.discard_pile = []
        return new_card_pile
