# This module defines the Player class which represents a player in a card game.


# Represents a player in a card game.
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # Removes and returns a card from the player's hand.
    def remove_one(self):
        return self.all_cards.pop(0)

    # Adds one or more cards to the player's hand.
    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
