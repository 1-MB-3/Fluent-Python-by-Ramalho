class Deck:

    def __init__(self):

        self.cards = []

        from itertools import product

        suits = ["♠", "♥", "♦", "♣"]
        ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

        for rank, suit in product(ranks, suits):

            self.cards.append(Card(rank, suit))

    def __len__(self):

        return len(self.cards)
    
    def __getitem__(self, i):

        return self.cards[i]
    
    def __setitem__(self, i, value):

        self.cards[i] = value

class Card:

    def __init__(self, rank, suit):

        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return self.rank + self.suit


deck=Deck()

print(len(deck))

for cards in deck:
    print(cards)

print(deck[5:10])

import random  
random.shuffle(deck)

print(deck[5:10])

print(random.choice(deck))

