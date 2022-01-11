class Card:
    def __init__(self,value,suit):
       # if type(value)!= int:
        #    raise TypeError("value must be of type int!")
     #   if type(suit) != int:
       #    raise TypeError("suit must be of type int!")
        self.value=value
        self.suit=suit


    def __gt__(self,other):
        #print("insid __gt__")
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
        suit={1:'Diamond',2:'Spade',3:'Heart',4:'Club'}
        values={1:'Ace',11:'Jack',12:'Queen',13:'King'}
        if self.value==1 or self.value==11 or self.value==12 or self.value==13:
            return f'{values[self.value]} {suit[self.suit]}'
        else:
            return f'{self.value} {suit[self.suit]}'
    def __eq__(self, other):
        if self.value==other.value:
            if self.suit==other.suit:
                return True
        return False

