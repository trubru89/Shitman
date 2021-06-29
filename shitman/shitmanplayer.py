from shitman.cardhand import CardHand


class Player(CardHand):

    def __init__(self):
        self.player_name = input("What is the player name? ")
        super().__init__()

    def get_player_name(self):
        return self.player_name

    @staticmethod
    def is_real_player():
        return True
