
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

    def remove_card(self, card_index):
        card_to_play = self.player_hand.pop(card_index)
        return card_to_play

    def remove_card_from_turn_up(self, card_index):
        card_to_play = self.player_turn_up.pop(card_index)
        return card_to_play

    def remove_card_from_turn_down(self, card_index):
        card_to_play = self.player_turn_down.pop(card_index)
        return card_to_play

    def number_of_cards_in_hand(self):
        return len(self.player_hand)

    # This should be in aishitman
    def get_lowest_card_in_hand(self):
        values_in_hand = [card.get_value() for card in self.player_hand]
        suits_in_hand = [card.get_suit() for card in self.player_hand]
        if len(values_in_hand) == len(set(values_in_hand)):  # if true contains duplicates,
            return min(values_in_hand)                       # if i wanna fix lowest + heart goes first
        else:
            card_index = values_in_hand.index(min(values_in_hand))
            return min(values_in_hand)

    # used to test remove card. Think of who to remove this from this class.
    # This function should not have to be here
    def get_card_from_hand(self):
        if self.player_hand:
            return self.player_hand[0]
        else:
            return False

    def card_hand_is_depleted(self):
        return False if self.player_hand else True

    def turn_up_is_depleted(self):
        return False if self.player_turn_up else True

    def turn_down_is_depleted(self):
        return False if self.player_turn_down else True
