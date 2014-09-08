
from enum import Enum
class Suit(Enum):
    CLUBS=1
    SPADES=2
    HEARTS=3
    DIAMONDS=4
    def __init__(self,val):
        self.value=val

class Card:
    def __init__(self,r,s):
        self.card=r
        self.suit=s

class BlackJackCard(Card):
    def __init__(self,r,s):
        super(BlackJackCard,self).__init__(r,s)
    def Value(self):
        if r==1: return 11;
        if r<10: return r;
        return 10


