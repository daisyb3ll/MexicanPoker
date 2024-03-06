import random
from collections import Counter
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Tuple

class Suit(enum):
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
class Rank(enum):
    Two = 2
    Three =3
    Four =4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10 
    JACK = 11
    QUEEN = 12 
    KING = 12 
    ACE = 13 

class pokerHand: 
    mylist = [card_1,card_2,card_3,card_4,card_5]