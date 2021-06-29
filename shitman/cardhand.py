
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

    def add_card_to_hand(self, card):
        self.player_hand.append(card)

    def show_card_hand(self):
        return self.player_hand

    def show_turn_up(self):
        return self.player_turn_up

    def show_turn_down(self):
        return self.player_turn_down

    def draw_card_from_hand(self, card_index):
        card_to_play = self.player_hand.pop(card_index)
        return card_to_play

    def draw_card_from_turn_up(self, card_index):
        card_to_play = self.player_turn_up.pop(card_index)
        return card_to_play

    def draw_card_from_turn_down(self, card_index):
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

    def card_distribution(self):
        return [len(self.player_hand), len(self.player_turn_up), len(self.player_turn_down)]

    def card_hand_is_depleted(self):
        return not self.player_hand

    def turn_up_is_depleted(self):
        return not self.player_turn_up

    def turn_down_is_depleted(self):
        return not self.player_turn_down

    def player_is_out_of_cards(self):
        return len(self.player_hand + self.player_turn_up + self.player_turn_down) == 0
