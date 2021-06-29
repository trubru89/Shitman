
class Card:

    def __init__(self, suit, value, rank):
        self.suit = suit
        self.value = value
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def get_rank(self):
        return self.rank
