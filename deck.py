# This module defines the Deck class which represents a deck of cards.

from card import Card, suits, ranks
import random


# Represents a deck of cards.
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(rank, suit)
                self.all_cards.append(Card(rank, suit))

    # Shuffles the deck.
    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    # Removes and returns a card from the deck.
    def deal_one(self):
        return self.all_cards.pop()
