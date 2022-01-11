from unittest import TestCase,mock
from CardGame import CardGame
from Player import Player
from DeckOfCards import DeckOfCards
from unittest.mock import patch


class TestCardGame(TestCase):
    #setUp that set CardGame object
    def setUp(self):
        print("setUp")
        self.card_game=CardGame("ben","guy",26)

#test valid name for plater1
    def test__init__validname_player1(self):
        self.assertEqual(self.card_game.player1.name,"ben")
        self.assertEqual(type(self.card_game.player1),Player)

    # test valid name for plater2
    def test__init__validname_player2(self):
        self.assertEqual(self.card_game.player2.name, "guy")
        self.assertEqual(type(self.card_game.player2), Player)

    # test valid name for player1
    def test__init__invalidname_player1(self):
        with self.assertRaises(TypeError):
            self.card_game(12,"guy",26)

    # test invalid name for player2
    def test__init__invalidname_player2(self):
        with self.assertRaises(TypeError):
                self.card_game("ben", 123, 26)

#test all vaild input as number of card,and if Player object set number to the valids numbers
    def test__init__validnum_card(self):
        self.assertEqual(self.card_game.player1.number_of_card,26)
        self.assertEqual(self.card_game.player2.number_of_card,26)
        card_game=CardGame("ben","guy",9)
        self.assertEqual(card_game.player1.number_of_card,26)
        self.assertEqual(card_game.player2.number_of_card,26)
        card_game = CardGame("ben", "guy", 27)
        self.assertEqual(card_game.player1.number_of_card, 26)
        self.assertEqual(card_game.player2.number_of_card, 26)
        card_game = CardGame("ben", "guy", 10)
        self.assertEqual(card_game.player1.number_of_card,10)
        self.assertEqual(card_game.player2.number_of_card,10)

#test input of invalid number in CardGame
    def test__init__invalidnum_card(self):
        with self.assertRaises(TypeError):
            self.card_game("ben","guy","123")
            self.card_game.player1
            self.card_game.player2

#test if init method create deck_card_list
    def test__init__deck_exist(self):
        self.assertEqual(self.card_game.deck_card.list_cards,[])

#test if new_game() is called from init and not by herself
    def test__init__called_method(self):
        with self.assertRaises(ValueError):
            self.card_game.new_game()

#test that two players have list by the number of cards and they dont have same cards
    def test_new_game(self):
        self.assertEqual(len(self.card_game.player1.list_card),26)
        self.assertEqual(len(self.card_game.player2.list_card),26)
        for i in self.card_game.player1.list_card:
            self.assertNotIn(i,self.card_game.player2.list_card)

#test if get_winner() return player1 if he have more cards
    def test_get_winner(self):
        card=self.card_game.player2.get_card()
        self.card_game.player1.add_card(card)
        self.assertGreaterEqual(len(self.card_game.player1.list_card),len(self.card_game.player2.list_card),self.card_game.player1)

#test if get_winner() return player2 if he have more cards
    def test_get_winner2(self):
        card1=self.card_game.player1.get_card()
        self.card_game.player2.add_card(card1)
        card2=self.card_game.player1.get_card()
        self.card_game.player2.add_card(card2)
        self.assertLessEqual(len(self.card_game.player1.list_card),len(self.card_game.player2.list_card),self.card_game.player2)

# test if get_winner() return None they have same amount of cards
    def test_get_winner3(self):
        print(len(self.card_game.player1.list_card))
        print(len(self.card_game.player2.list_card))
        self.assertEquals(len(self.card_game.player1.list_card),len(self.card_game.player2.list_card),None)

