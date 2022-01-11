# Produces a card in a card game
class Card:
    # Gets value and suit
    def __init__(self,value,suit):
        if type(value)!= int:
            raise TypeError("value must be of type int!")
        if type(suit) != int:
            raise TypeError("suit must be of type int!")
        self.value=value
        self.suit=suit

# Checks if the current card is larger than the card you received
    def __gt__(self,other):
        # Defines the number 1 (Ace) highest card
        if self.value>other.value:
            if other.value==1:
                return False
            else:
                return True
        elif self.value<other.value:
            if self.value==1:
                return True
            else:
                return False

        if self.suit>other.suit:
            return True
        elif self.suit<other.suit:
            return False


    def __repr__(self):
        suit={1:'Diamond',2:'Spade',3:'Heart',4:'Club'}# Defines a number for each suit
        values={1:'Ace',11:'jack',12:'Queen',13:'King'} # Defines a number for each values
        if self.value==1 or self.value==11 or self.value==12 or self.value==13:
            return f'{values[self.value]} {suit[self.suit]}'

        return f'{self.value} {suit[self.suit]}'
    # Defines whether the value is equal to other value
    def __eq__(self, other):
        if type(other)!= Card:  # The other value must be a card value

            raise TypeError("other must be of type card!")

        if self.value==other.value:

            if self.suit==other.suit:
                return True

        return False





