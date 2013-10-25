# Listing_11-1.py  
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Printing three multiplication tables at once

for multiplier in range (5, 8):
    for i in range (1, 11):
        print i, "x", multiplier, "=", i * multiplier 
    print