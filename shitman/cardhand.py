
class CardHand:

    def __init__(self):
        self.player_hand = []
        self.pos_in_hand = 0
        self.card_to_remove = None
        self.player_turn_up = []
        self.player_turn_down = []

    def get_start_hand(self, player_start_hand):
        self.player_hand = player_start_hand

    def get_player_turn_up(self, player_turn_up):
        self.player_turn_up = player_turn_up

    def get_player_turn_down(self, player_turn_down):
        self.player_turn_down = player_turn_down

    def add_card(self, card):
        self.player_hand.append(card)

    def remove_card(self, card):
        if card in self.player_hand:
            self.pos_in_hand = self.player_hand.index(card)
            self.card_to_remove = self.player_hand[self.pos_in_hand]
            self.player_hand.pop(self.card_to_remove)
            return self.card_to_remove
        else:
            return False

