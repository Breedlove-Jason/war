from card import Card
from deck import Deck


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


# new_player = Player("Jose")
# print(new_player)
# my_card = Deck().deal_one()
# # new_player.add_cards(Card("3", "Hearts"))
# new_player.add_cards([my_card, my_card, my_card])
# print(new_player)
# for card in new_player.all_cards:
#     print(card)
#
# new_player.remove_one()
# print(new_player)
