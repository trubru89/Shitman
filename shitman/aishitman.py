from shitman.cardhand import CardHand


class AiPlayer(CardHand):

    def __init__(self):
        super().__init__()

    def ai_play_card(self, current_card_in_pile_value):
        pass

    @staticmethod
    def is_real_player():
        return False
