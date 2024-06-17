from card import Card, suits, ranks
from deck import Deck
from player import Player


player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")
    if not player_one.all_cards:
        print("Player One, out of cards! Player Two wins!")
        game_on = False
        break
    if not player_two.all_cards:
        print("Player Two, out of cards! Player One wins!")
        game_on = False
        break

    player_one_cards = [player_one.remove_one()]
    player_two_cards = [player_two.remove_one()]
