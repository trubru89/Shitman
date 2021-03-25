from shitman import cardhand


class Player(cardhand.CardHand):

    def __init__(self):
        super().__init__()
        self.pos_of_card_to_play = None
        self.card_to_play = None

    def select_card_to_play(self):
        print("Player hand is: ")
        for card in self.player_hand:
            print(card.suit)
            print(card.value)
        self.pos_of_card_to_play = int(input("Chose card to play (1,2,3...): "))
        self.card_to_play = self.player_hand((self.pos_of_card_to_play-1))
        self.remove_card(self.card_to_play)
        return self.card_to_play
