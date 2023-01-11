# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_card.ipynb 4
from fastcore.utils import *
suits = "♠♥♦♣"
ranks = [None,"A"] + [str(x) for x in range(2,11)] + ["J","Q","K"]

# %% ../nbs/00_card.ipynb 14
class Card:
    "A playing card"
    def __init__(self,
                 suit:int,  # An index into suits
                 rank:int): # An index into ranks
   

     self.suit,self.rank = suit,rank
    def __str__(self): return f"{ranks[self.rank]}{suits[self.suit]}" 
    __repr__ = __str__

# %% ../nbs/00_card.ipynb 19
@patch    
def __gt__(self: Card,o: Card): return (self.suit,self.rank)>(o.suit,o.rank)

@patch    
def __eq__(self: Card,o: Card): return (self.suit,self.rank)==(o.suit,o.rank)

@patch    
def __lt__(self: Card,o: Card): return (self.suit,self.rank)<(o.suit,o.rank)