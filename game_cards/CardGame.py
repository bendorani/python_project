from Player import Player
from DeckOfCards import DeckOfCards
from Card import Card
class CardGame:
    #constructor method that get two names and number of cards(by default 26) and build two player objects
    #and DeckOfCards object and call her method new game
    def __init__(self,name1,name2,num_of_cards=26):
        if type(name1)!=str:
            raise TypeError("name must be str")
        if type(name2)!=str:
            raise TypeError("name must be str")
        if type(num_of_cards) != int:
            raise TypeError("number of cards must be int")
        self.player1=Player(name1,num_of_cards)
        self.player2=Player(name2,num_of_cards)
        self.deck_card=DeckOfCards()
        self.new_game()
#this method using cards_shuffle method to shuffle deck and set the players list with cards from deck
    def new_game(self):
#check if the method didnt called after starting the game, if yes she give error message
        if self.player1.list_card==[]:
            self.deck_card.cards_shuffle()
            self.player1.set_hand(self.deck_card)
            self.player2.set_hand(self.deck_card)
        else:
            raise ValueError("you cant call the method")
    #this method return the player with the most cards if they both have same amount return none
    def get_winner(self):
        if len(self.player1.list_card)>len(self.player2.list_card):
            return self.player1
        elif len(self.player1.list_card)<len(self.player2.list_card):
            return self.player2
        elif len(self.player1.list_card)==len(self.player2.list_card):
            return None
    #this method return the details of players
    def __repr__(self):
        return f"player1:{self.player1}\nplayer two:{self.player2}"