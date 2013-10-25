# Listing_11-3  
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Blocks of stars with double-nested loops

numBlocks = int(raw_input ('How many blocks of stars do you want? '))
numLines = int(raw_input ('How many lines in each block? '))
numStars = int(raw_input ('How many stars per line? '))
for block in range (0, numBlocks):
    for line in range (0, numLines):
        for star in range (0, numStars): 
            print '*',
        print
    print
