

class CardPile:

    def __init__(self):
        self.card_pile = []
        self.top_card = None

    def add_to_card_pile(self, card):
        self.card_pile.insert(0, card)

    def throw_card_pile(self):
        cards_to_throw = [a_card for a_card in self.card_pile]
        self.card_pile = []
        return cards_to_throw

    def show_top_card_in_card_pile(self):
        if self.card_pile:
            self.top_card = self.card_pile[0]
            return self.top_card
        else:
            return False
