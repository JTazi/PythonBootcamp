# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:55:42 2022

@author: tazma
"""

# playing card class

class playingCard(object):
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
        
    def display(self):
        print(f'Your Card is {self.value} of {self.suit}')
        
    def __str__(self):
        suit_dict = {'d':'Diamonds',
                'h':'Hearts',
                's':'Spades',
                'c':'Clubs'}
        my_card = str(self.value) + ' of ' + suit_dict[self.suit]
        return my_card