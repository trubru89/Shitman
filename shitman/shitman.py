import carddeck


def main():
    card_deck = carddeck.CardDeck()
    card_deck.compile_deck()
    #card_deck.show_deck()
    card_deck.shuffle_deck()
    #card_deck.show_deck()
    card_deck.draw_from_deck()
    #card_deck.show_deck()


if __name__ == "__main__":
    main()
