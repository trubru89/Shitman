from shitman import cardhand


class Player(cardhand.CardHand):

    def __init__(self):
        super().__init__()
        self.card_to_play_from_hand = None

    def select_card_to_play(self):
        print("Player hand is ", self.player_hand)
        self.card_to_play_from_hand = input("Chose card to play: ")

