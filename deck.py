#this is the poker deck
#this deals with how the deck is generated, and how it is shuffled, and it also creates the randomized draw
#uses dictionaries to sort the suits, decks, and numbers

import random
from random import randint

import unittest
from deck import draw_cards

suits= {
    0: '♣',
    1: '♦',
    2: '♥',
    3: '♠'
}

cards = {
    0: 'A',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: '10',
    10: 'J',
    11: 'Q',
    12: 'K',
}

def draw_cards(num_of_cards, list_dealt=[]):
    for z in range(num_of_cards):
        x = randint(0,3) #random integer 0 to 3 to pick suit
        y = randint(0,12) #random integer 0 to 12 to pick card
        mycard = "{0} of {1}".format(cards[y],suits[x])
        if mycard not in list_dealt:
            list_dealt.append(mycard)
        else:
            num_of_cards = num_of_cards - z
            return draw_cards(num_of_cards,list_dealt)
            
    return list_dealt

mydraw = draw_cards(5) #call the function with the number of cards you want. 

i = 0
for x in mydraw:
    i += 1
    if i == len(mydraw):
        print("your last card is {0}".format(str(x)))
    else:
        print("You got the {0}".format(str(x)))
