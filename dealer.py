#dealer.py 
# intended to act as a poker dealer, this is what (1)shuffles the cards,(2) deals cards into poker hands, and (3)hands out cards when asked
import random

#shuffling cards
thislist = ["apple", "banana", "cherry"]

#(1)shuffles the cards
def shuffle_cards(deck):
    random.shuffle(deck)
    print(deck)
    return deck

#(2)deals cards into poker hands
def deal_card(deck):
    card_list = []
    for 5 in deck:
        card_list = deck.pop(0)
    return card_list
