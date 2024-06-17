from card import Card, suits, ranks
import random


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(rank, suit)
                self.all_cards.append(Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# new_deck = Deck()
# new_deck.shuffle_deck()
# for card in new_deck.all_cards:
#     print(card)
#
# print(new_deck.deal_one())
