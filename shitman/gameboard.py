from shitman.carddeck import CardDeck
from shitman.shitmanplayer import Player
from shitman.aishitman import AiPlayer
from shitman.cardpile import CardPile
from shitman.discardpile import DiscardPile


class GameBoard:

    def __init__(self, number_of_players=2, number_of_ai=0):
        self.number_of_real_players = number_of_players
        self.number_of_ai = number_of_ai
        self.game_deck = CardDeck()
        self.game_deck.compile_deck()
        self.existing_players = []
        self.temp_cards = []
        self.card_pile = CardPile()
        self.discard_pile = DiscardPile()

    def set_up_players(self):
        for player in range(self.number_of_real_players):
            self.existing_players.append(Player())
        for ai in range(self.number_of_ai):
            self.existing_players.append(AiPlayer())
        return [player for player in self.existing_players]

    def shuffle_board_deck(self):  # pointless use game_deck shuffle insead
        self.game_deck.shuffle_deck()

# Below 3 functions should be one function...
    def get_player_start_hand(self):
        return [self.game_deck.draw_from_deck() for self.draw_card in range(3)]

    def get_player_turndown(self):
        return [self.game_deck.draw_from_deck() for self.draw_card in range(3)]

    def get_player_turnup(self):
        return [self.game_deck.draw_from_deck() for self.draw_card in range(3)]

    def draw_from_game_deck(self):
        return self.game_deck.draw_from_deck()

    def game_deck_is_not_depleted(self):
        return self.game_deck.deck_is_not_depleted()

    def add_to_card_pile(self, card):
        self.card_pile.add_to_card_pile(card)

    def discard_card_pile(self):
        self.discard_pile.add_to_discard_pile(self.card_pile.throw_card_pile())

    def top_card_in_card_pile(self):
        return self.card_pile.get_top_card_in_card_pile()

    def get_card_pile(self):
        return self.card_pile.throw_card_pile()

    def player_draw_card(self, player):
        if self.game_deck.deck_is_not_depleted():
            player.add_card_to_hand(self.game_deck.draw_from_deck())
