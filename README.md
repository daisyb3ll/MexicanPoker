# MexicanPoker
welcome to mexican poker, just like Texas Holdem- but not boring! 
The rule to Mexican Poker are very similar to regular poker. 

#SetUp
Fork Repository
    tutorial: 
    https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo

    terminal commands:
    python3 deck.py

    at the moment the only file that compiles and runs output is deck.py
    the rest of the game is still in progress
    
    

~~ CARDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To start, poker is a card game- we use cards. Poker is played with a deck of 52 cards. 
The deck of 52 cards has four different suits. Suits are the symbols on the cards. 
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
There is no rank order to these suits. 

Cards in the deck range from 2-10, and then JACK,QUEEN,KING, and ACE.
A deck of cards includes 13 ranks of each suit with reversible "court" or face cards. 
    Two = 2
    Three =3
    Four =4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10 
    !!!! and then we remix here by adding the face/court cards !!!!
    JACK = 11
    QUEEN = 12 
    KING = 12 
    ACE = 13 

~~ GAMEPLAY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Each player is dealt a hand of five cards. After everyone has had a chance to look at their hand, a betting round is played in which eveyone is allowed to either match or raise the betting pool. 
    Players are then allowed to ask to either
        Deal:
        A designated player (the dealer), is put in charge of deealing each player a set of five random cards.
        In the case of Mexican Poker, unlike regular poker- the eight, nine, and ten, cards are removed to
            (1) make the game faster
            and
            (2) make the game more competitive

        Hand:
        Once dealt, the players are allowed to view their cards, this goes the same way as regular poker. 
        The players the check their hand for any pattern of hands:
        hand terminology:
            flush: a flush is when you have all 5 cards of the same suit
            straight flish: a flush when the cards are in asceding/descending order
            royal flush: a flush that contains all of the court cards
            full house: having a three of a kind, plus any other two matching cards
        *************LIST OF HANDS *****************
        (in order from best to worst-ish)
            Royal Flush: 
                10,J,Q,K
            Straight Fush (but all of the same symbol): 
                (1,2,3,4,5),(2,3,4,5,6),(3,4,5,6,7),(5,6,7,J,K),(6,7,J,K,Q),(7,J,Q,K,A)
            Four of a Kind (in order from best to worst) :
                (A,A,A,A,x)(K,K,K,K,x),(Q,Q,Q,Q,x),(J,J,J,J,x),(7,7,7,7,x),(6,6,6,6,x)
                (5,5,5,5,x),(4,4,4,4,x),(3,3,3,3,x),(2,2,2,2,x)
            Full House:
                (A,A,A,X,x)(K,K,K,x,x),(Q,Q,Q,x,x),(J,J,J,x,x),(7,7,7,x,x),(6,6,6,x,x)
                (5,5,5,x,x),(4,4,4,x,x),(3,3,3,x,x),(2,2,2,x,x) 
            Flush: 
                (x,x,x,x,x) but all of the same ♠,♥,♦,♣
            Straight (cards in ascending order):
                (1,2,3,4,5),(2,3,4,5,6),(3,4,5,6,7),(5,6,7,J,K),(6,7,J,K,Q),(7,J,Q,K,A)
            Three of a Kind: 
                (1,1,1,x,x),(2,2,2,x,x),(3,3,3,x,x),(4,4,4,x,x),(5,5,5,x,x),(6,6,6,x,x),(7,7,7,x,x)...
            Two Pair:
                (y,y,y,x,x).. etc
            High Card:  
                this means your deck has nothing of value except for the highest value card. "king high"
        Special Exceptions: 
            The joker card is considered a wild card.


