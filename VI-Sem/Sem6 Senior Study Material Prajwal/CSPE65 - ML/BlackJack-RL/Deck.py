from numpy import random


class Deck:
    def __init__(self, n_decks=1):
        self.deck = []
        for i in range(0, n_decks):
            for number in range(1, 14):
                for suit in ['S', 'C', 'H', 'D']:
                    self.deck.append(Card(suit, number))

        self.shuffle_deck()

    def add_card(self, card):
        self.deck.append(card)

    def remove_card(self, card):
        self.deck.remove(card)

    def pop_card(self):
        return self.deck.pop()

    def shuffle_deck(self):
        random.shuffle(self.deck)


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def get_value(self):
        return min(self.number, 10)

    def get_suit(self):
        return self.suit

    def get_color(self):
        if self.suit == 'S' or self.suit == 'C':
            return 'black'

        return 'red'

    def get_suit_value(self):
        if self.suit == 'S':
            return 0
        if self.suit == 'C':
            return 1
        if self.suit == 'H':
            return 2
        return 3

    def get_number(self):
        return self.number
