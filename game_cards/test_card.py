from unittest import TestCase
from Card import *
from DeckOfCards import *

class TestCard(TestCase):
    def setUp(self):
        self.Card=Card(8,2)

    def tearDown(self):
        print('tearDown')

# Valid card values
    def test__init__(self):
        self.assertEqual(self.Card.value,8)
        self.assertEqual(self.Card.suit,2)

# Invalid card values
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            Card(8, 'ddd')
        with self.assertRaises(TypeError):
            Card('GGG',2)

#  the card is larger than the other value
    def test__gt__1(self):
        card1=Card(6,2)
        self.assertTrue(self.Card>card1)

# the other value is greater than the card
    def test__gt__2(self):
        card2=Card(10,2)
        self.assertTrue(self.Card<card2)

# Checks that the value is equal-'Ace'
    def test__gt__3(self):
        card3=Card(1,2)
        self.assertTrue(self.Card<card3)

# Checks that the value is equal-'Ace'
    def test__gt__4(self):
        card4=Card(12,3)
        card5=Card(1,4)
        self.assertTrue(card4<card5)

# Check that the function returns true
    def test__eq__valid_True(self):
        Card1 = Card(8, 2)
        Card2 = Card(8, 2)
        self.assertTrue(Card1==Card2)

# Check that the value of the tickets is not equal
    def test__eq__valid_False(self):
        Card1 = Card(6, 2)
        Card2 = Card(8, 2)
        self.assertFalse(Card1 == Card2)

# Check that the value of the tickets is not equal
    def test__eq__valid_False_1(self):
        Card1 = Card(8, 2)
        Card2 = Card(6, 2)
        self.assertFalse(Card1 == Card2)

# Check that the suit of the tickets is not equal
    def test__eq__valid_False_2(self):
        Card1 = Card(8, 1)
        Card2 = Card(8, 3)
        self.assertFalse(Card1 == Card2)

# Check that the suit of the tickets is not equal
    def test__eq__valid_False_3(self):
        Card1 = Card(8, 3)
        Card2 = Card(8, 1)
        self.assertFalse(Card1 == Card2)
# A test that inserts values that are not int
    def test__eq__invalid(self):
        with self.assertRaises(TypeError):
            Card(8, 'ddd')
        with self.assertRaises(TypeError):
            Card('GGG',2)






