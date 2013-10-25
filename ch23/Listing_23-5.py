# Listing_23-5.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Making a deck or cards

import random
from cards import Card

deck = []                                           
for suit_id in range(1, 5):                           
    for rank_id in range(1, 14):    
        deck.append(Card(suit_id, rank_id))        

hand = []                                           
for cards in range(0, 5):                          
    a = random.choice(deck)                         
    hand.append(a)                                  
    deck.remove(a)                                  

print    
for card in hand:
    print card.short_name, '=' ,card.long_name, "  Value:", card.value