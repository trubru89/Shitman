from shitman import cardhand


class Player(cardhand.CardHand):

    def __init__(self):
        super().__init__()
        self.pos_of_card_to_play = None
        self.card_to_play = None

    def select_where_to_draw_card(self):
        if self.player_hand:
            return self.select_card_to_play()
        else:
            if self.player_turn_up:
                return self.select_card_from_turn_up()
            else:
                if self.player_turn_down:
                    return self.select_card_from_turn_down()
                else:
                    return True

    def select_card_to_play(self, played_card=None):
        print("Played card is: " + played_card.suit + played_card.value) if played_card is not None \
            else print("No card is played ")
        print("Player hand is: ")
        for card in self.player_hand:
            print(card.suit)
            print(card.value)
        self.pos_of_card_to_play = int(input("Chose card to play (1,2,3...): "))
        self.card_to_play = self.player_hand((self.pos_of_card_to_play-1))
        self.remove_card(self.card_to_play)
        return self.card_to_play

    def select_card_from_turn_up(self, played_card=None):
        pass

    def select_card_from_turn_down(self, played_card=None):
        pass

    @staticmethod
    def is_real_player():
        return True
