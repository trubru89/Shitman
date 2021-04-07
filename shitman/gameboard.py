from shitman import carddeck
from shitman import shitmanplayer
from shitman import aishitman


class GameBoard:

    def __init__(self, number_of_players=1, number_of_ai=1):
        self.number_of_real_players = number_of_players
        self.number_of_ai = number_of_ai
        self.game_deck = carddeck.CardDeck()
        self.game_deck.compile_deck()
        self.existing_players = []
        self.temp_cards = []

    def set_up_players(self):
        for player in range(self.number_of_real_players):
            self.existing_players.append(shitmanplayer)
        for ai in range(self.number_of_ai):
            self.existing_players.append(aishitman)
        return self.existing_players

    def shuffle_board_deck(self):
        self.game_deck.shuffle_deck()

    def get_player_start_hand(self):
        return [self.game_deck.draw_from_deck() for draw_card in range(3)]

    def get_player_turndown(self):
        return [self.game_deck.draw_from_deck() for draw_card in range(3)]

    def get_player_turnup(self):
        return [self.game_deck.draw_from_deck() for draw_card in range(3)]

    def draw_from_game_deck(self):
        return self.game_deck.draw_from_deck()

    def game_deck_is_depleted(self):
        return self.game_deck.deck_is_depleted()
