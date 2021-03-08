import carddeck


class GameBoard:

    def __init__(self, number_of_players=1, number_of_ai=1):
        self.number_of_real_players = number_of_players
        self.number_of_ai = number_of_ai
        self.number_of_players = number_of_players + number_of_ai
        self.game_deck = None
        self.player_turndown = {}
        self.player_turnup = {}
        self.discard_pile = []
        self.player_start_hands = {}

    def set_up_players(self):
        for player in range(self.number_of_players):
            self.player_turndown[player] = []
        for player in range(self.number_of_players):
            self.player_turnup[player] = []

    def set_up_board(self):
        self.game_deck = carddeck.CardDeck()
        self.game_deck.shuffle_deck()
        for key in self.player_turndown:
            for cards_in_turndown in range(3):
                self.player_turndown[key].append(self.game_deck.draw_from_deck())
        for key in self.player_turnup:
            for cards_in_turnup in range(3):
                self.player_turnup[key].append(self.game_deck.draw_from_deck())
        for player in range(self.number_of_players):
            for cards_in_hand in range(3):
                self.player_start_hands[player].append(self.game_deck.draw_from_deck())

    def draw_from_game_deck(self):
        if self.game_deck:
            drawn_card = self.game_deck[0]
            self.game_deck.pop(0)
            return drawn_card
        else:
            print("out of cards")
            return False
