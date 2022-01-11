import random
from Card import *

# Contains the property of an entire deck of cards
class DeckOfCards:

    # Creates a pack of 52 different cards
    def __init__(self):
        self.list_cards=[]
        for i in range(1,14):
            for j in range(1,5):
                card=Card(i,j)
                self.list_cards.append(card)

# Randomly shuffles the list of cards
    def cards_shuffle(self):
        random.shuffle(self.list_cards)

# Pulls a random card from the list
    def deal_one(self):
        card_random=random.choice(self.list_cards)
        self.list_cards.remove(card_random)
        return card_random

    def __repr__(self):
        return f'{self.list_cards}'









