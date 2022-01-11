from unittest import TestCase,mock
from Player import Player
from unittest.mock import patch
from DeckOfCards import DeckOfCards


from Card import Card

class TestPlayer(TestCase):
    #setUp that set a player object and deck
    def setUp(self):
        self.player=Player("ben",26)
        self.deck = DeckOfCards()
        print("SetUp")

#test if player name get in player
    def test__init__validname(self):
        self.assertEqual(self.player.name,"ben")

#test invalid type name
    def test__init__invalidname(self):
        with self.assertRaises(TypeError):
            self.player1=Player(123,26)

#test all valid options you can input to player, ערכי קצה
    def test__init__validnumber_Card(self):
        self.assertEqual(self.player.number_of_card,26)
        player1=Player("ben",9)
        self.assertEqual(player1.number_of_card,26)
        player1=Player("BEN",27)
        self.assertEqual(player1.number_of_card,26)
        player1=Player("ben",10)
        self.assertEqual(player1.number_of_card,10)
        player1=Player("ben",)
        self.assertEqual(player1.number_of_card,26)

#test invalid number card as input to player
    def test__init__invalidnumber_card(self):
        with self.assertRaises(TypeError):
            self.player1=Player("ben","aaa")

#test if the init method crate list
    def test__init__listexist(self):
        self.assertEqual(self.player.list_card,[])

#using mock as deal_one function, check if the card that dealed enter player list cards
    def test_set_hand_valid(self):
        with patch('DeckOfCards.DeckOfCards.deal_one')as mock_deal_one:
            mock_deal_one.return_value="Ace Diamond"
            player1 = Player("BEN", 10)
            player1.set_hand(self.deck)
            print(player1.list_card)
            self.assertIn("Ace Diamond",player1.list_card)

# using mock as deal_one function, check if player lists' len is set by number of cards
    def test_set_hand_validlen(self):
        with patch('DeckOfCards.DeckOfCards.deal_one')as mock_deal_one:
            mock_deal_one.return_value="Ace Diamond"
            player1 = Player("BEN", 10)
            player1.set_hand(self.deck)
            self.assertEqual(len(player1.list_card),10)

#test for invalid deck type
    def test_set_hand_invalid(self):
        with self.assertRaises(TypeError):
            self.player.set_hand(10)
        with self.assertRaises(TypeError):
            self.player.set_hand("aaa")

#test if method get card pull out the card from the list
    def test_get_card_valid(self):
        card1 = Card(2, 3)
        card2 = Card(4, 3)
        card3 = Card(5, 3)
        card4 = Card(11, 3)
        self.player.list_card = [card1, card2, card3, card4]
        card=self.player.get_card()
        self.assertNotIn(card,self.player.list_card)

#test if get_card() remove card from list
    def test_get_card_validlen(self):
        card1 = Card(2, 3)
        card2 = Card(4, 3)
        card3 = Card(5, 3)
        card4 = Card(11, 3)
        self.player.list_card = [card1, card2, card3, card4]
        card = self.player.get_card()
        self.assertEqual(len(self.player.list_card),3)

#test calling function when player dont have list of cards
    def test_get_card_invalid(self):
        player3=Player("ben",10)
        with self.assertRaises(ValueError):
            player3.get_card()

#test if add_card()adding card to player list
    def test_add_card_valid(self):
        card1= Card(2,3)
        card2= Card(4,3)
        card3= Card(5,3)
        card4= Card(11,3)
        self.player.list_card=[card1,card2,card3,card4]
        card=Card(3,2)
        self.player.add_card(card)
        self.assertIn(card,self.player.list_card)

#test if add_card() add some cards and players list is changed
    def test_add_card_validlen(self):
        card1 = Card(2, 3)
        card2 = Card(4, 3)
        card3 = Card(5, 3)
        card4 = Card(11, 3)
        self.player.list_card = [card1, card2, card3, card4]
        card = Card(3, 2)
        lenth = len(self.player.list_card)
        self.player.add_card(card)
        card5=Card(12,1)
        self.player.add_card(card5)
        self.assertEqual(len(self.player.list_card), lenth + 2)
        self.assertIn(card5,self.player.list_card)

#test if adding card that player already have dont add to player list
    def test_add_card_cardinlist(self):
        card1 = Card(2, 3)
        card2 = Card(4, 3)
        card3 = Card(5, 3)
        card4 = Card(11, 3)
        self.player.list_card = [card1, card2, card3, card4]
        card = Card(2, 3)
        lenth = len(self.player.list_card)
        self.player.add_card(card)
        self.assertEqual(len(self.player.list_card),lenth)

#test input invalid type of Card
    def test_add_card_invalid(self):
        with self.assertRaises(TypeError):
            self.player.add_card(10)
        with self.assertRaises(TypeError):
            self.player.add_card("asas")



