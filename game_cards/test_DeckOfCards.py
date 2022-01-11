from unittest import TestCase
from Card import *
from DeckOfCards import *

class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck=DeckOfCards()

    def tearDown(self):
        print('tearDown')

# Checks that no two cards are the same on the list
    def test__init__(self):
        for i in range(1,14):
            for j in range(1,5):
                card=Card(i,j)
                self.assertIn(card,self.deck.list_cards)

# Checks that the list length is 52 cards
    def test__init__1(self):
        list_cards = []
        for i in range(1, 14):
            for j in range(1, 5):
                card = Card(i, j)
                list_cards.append(card)
        self.assertEqual(len(list_cards),52)

# Checking that the list is mixed
    def test_cards_shuffle(self):
        list1=self.deck.list_cards
        self.deck.cards_shuffle()
        self.assertNotEqual(self.deck.cards_shuffle,list1) # The original list and the new list are different

# Checker removes a card from the list
    def test_deal_one(self):
        list = self.deck.list_cards
        card2=self.deck.deal_one()
        self.assertNotIn(card2,self.deck.list_cards) # Checks that the card is not on the list


