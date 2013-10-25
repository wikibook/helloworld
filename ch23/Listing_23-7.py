# Listing_23-7.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Crazy Eights - Display what is in the player's hand

# Note that this is not a complete program.  It needs to be put together
#   with the other parts of Crazy Eights to make a working program.

print "\nYour hand: ",
for card in p_hand:
    print card.short_name,
print "   Up card: ", up_card.short_name
if up_card.rank == '8':
    print"   Suit is", active_suit 
