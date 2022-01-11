from random import choice
from DeckOfCards import DeckOfCards
from Card import Card
class Player:

    #this method get name, and number of card(by default 26) and set empty list
    def __init__(self,name,number_of_cards=26):
        #check if name is the right type
        if type(name)!=str:
            raise TypeError("name must be string")
        #check if number of card is the right type
        if type(number_of_cards)!=int:
            raise TypeError("number of cards must be int")
        self.name=name
        self.number_of_card=number_of_cards
        #set the number of card to 26 if is smaller than 10 or above 26
        if self.number_of_card>26 or self.number_of_card<10:
            self.number_of_card=26
        self.list_card=[]


       #get object type DeckOfCards and uses the deal_one method to set player list of cards
    def set_hand(self,deck:DeckOfCards):
    #check if the method got the right object
        if type(deck)!=DeckOfCards:
            raise TypeError("set hand must get deckofcards object")
        for i in range(self.number_of_card):
            self.list_card.append(deck.deal_one())


    #this method uses radom functaion to choose randomly a card from player list cards and return the card
    def get_card(self):
    #check if method not called if there is no cards to player
        if self.list_card==[]:
            raise ValueError("you dont have cards in your hand")
        card=choice(self.list_card)
    #removing the card from the player list when he pulled it out
        self.list_card.remove(card)
        return card


    #this method get card object and add it to player list cards
    def add_card(self,card:Card):
    #check if the method got Card object
        if type(card)!=Card:
            raise TypeError("card must be Card object")
        if card not in self.list_card:
            self.list_card.append(card)


    #this method return the player details
    def __repr__(self):
        return f"player name:{self.name} list card:{self.list_card}"
