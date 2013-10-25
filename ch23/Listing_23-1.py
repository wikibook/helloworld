# Listing_23-1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Rolling a single 11-sided die 1000 times.

import random

totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]                   
for i in range(1000):
    dice_total = random.randint(2, 12)
    totals[dice_total] += 1                                         
    
for i in range (2, 13):
    print "total", i, "came up", totals[i], "times"