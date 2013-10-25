# Listing 11-5
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Printing the loop variables in nested loops

numBlocks = int(raw_input('How many blocks of stars do you want? '))
for block in range (1, numBlocks + 1):
    print 'block = ', block
    for line in range (1, block * 2 ):
        for star in range (1, (block + line) * 2): 
            print '*',
        print '  line = ', line, 'star = ', star    # display variables
    print
