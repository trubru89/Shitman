

class CardPile:

    def __init__(self):
        self.card_pile = []
        self.top_card = None

    def add_to_card_pile(self, card):
        self.card_pile.insert(0, card)

    def draw_from_card_pile(self, discarded_pile):
        if self.card_pile:
            card_to_draw = self.card_pile.pop(0)
            return card_to_draw
        else:
            self.card_pile = discarded_pile
            self.draw_from_card_pile(discarded_pile)

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
