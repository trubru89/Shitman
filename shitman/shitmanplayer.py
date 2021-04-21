from shitman.cardhand import CardHand


class Player(CardHand):

    def __init__(self):
        super().__init__()
        self.pos_of_card_to_play = None
        self.card_to_play = None

    def select_where_to_draw_card(self, played_card_in_pile):
        if self.player_hand:
            return self.select_card_to_play(played_card_in_pile)
        else:
            if self.player_turn_up:
                return self.select_card_from_turn_up(played_card_in_pile)
            else:
                if self.player_turn_down:
                    return self.select_card_from_turn_down(played_card_in_pile)
                else:
                    return False

# below 3 should be 1 function
    def select_card_to_play(self, played_card=None):
        print("Played card is: " + played_card.suit + played_card.value) if played_card is not None \
            else print("No card is played ")
        print("Player hand is: ")
        for card in self.player_hand:
            print(card.suit)
            print(card.value)
        self.pos_of_card_to_play = int(input("Chose card to play (1,2,3...): "))
        card_to_play = self.remove_card(self.pos_of_card_to_play-1)
        return card_to_play

    def select_card_from_turn_up(self, played_card=None):
        print("Played card is: " + played_card.suit + played_card.value) if played_card is not None \
            else print("No card is played ")
        print("Player turn up is: ")
        for card in self.player_turn_up:
            print(card.suit)
            print(card.value)
        self.pos_of_card_to_play = int(input("Chose card to play (1,2,3...): "))
        card_to_play = self.remove_card_from_turn_up(self.pos_of_card_to_play - 1)
        return card_to_play

    def select_card_from_turn_down(self, number_of_cards_in_turn_down, played_card=None):
        print("Played card is: " + played_card.suit + played_card.value) if played_card is not None \
            else print("No card is played ")
        print("Number of card to choose from in turn down: {}".format(number_of_cards_in_turn_down))
        self.pos_of_card_to_play = int(input("Chose card to play (1,2,3...): "))
        card_to_play = self.remove_card_from_turn_down(self.pos_of_card_to_play-1)
        return card_to_play

    @staticmethod
    def is_real_player():
        return True
