class Deck:     #class, which we will be using throught this code

    def __init__(self):     #adding values to cards

        self.cards = []       #using cards from Deck

        from itertools import product       #itertools is like pair in C++

        suits = ["♠", "♥", "♦", "♣"]
        ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

        for rank, suit in product(ranks, suits):

            self.cards.append(Card(rank, suit))     #adding all values

    def __len__(self):      #returning length of cards

        return len(self.cards)
    
    def __getitem__(self, i):       #returning values for i cell

        return self.cards[i]
    
    def __setitem__(self, i, value):    #setting values for cards

        self.cards[i] = value

class Card:     #case in which we want to get one value (combined rank and suit) in our output

    def __init__(self, rank, suit):

        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return self.rank + self.suit


deck=Deck()     #acessing our class and assigning it to variable

print(len(deck))        #it works, because we use len dunder in the Deck class

for cards in deck:      #it works, because for checks till IndexError, so it will check every cell till it finds it
    print(cards)

print(deck[5:10])       #checking from deck[5] till deck[9]

import random  
random.shuffle(deck)        #shuffling deck

print(deck[5:10])       #checking if shuffle worked

print(random.choice(deck))      #picking random card

