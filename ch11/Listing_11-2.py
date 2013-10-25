# Listing_11-2.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# A variable nested loop

numLines = int(raw_input ('How many lines of stars do you want? '))
numStars = int(raw_input ('How many stars per line? '))
for line in range (0, numLines):
    for star in range (0, numStars): 
        print '*',
    print
