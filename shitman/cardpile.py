from shitman.card import Card


class CardPile:

    def __init__(self):
        self.card_pile = []
        self.empty_card = Card("No suit", 0, "No rank")
        self.top_card = self.empty_card

    def add_to_card_pile(self, card):
        self.card_pile.insert(0, card)

    def throw_card_pile(self):
        cards_to_throw = self.card_pile
        self.card_pile = []
        return cards_to_throw

    def get_top_card_in_card_pile(self):
        if self.card_pile:
            self.top_card = self.card_pile[0]
            return self.top_card
        else:
            self.top_card = self.empty_card
            return self.top_card
