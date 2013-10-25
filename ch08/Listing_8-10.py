# Listing_8-10.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Using break in a loop

for i in range (1, 6):
    print
    print 'i =', i,
    print 'Hello, how',
    if i == 3:
        break                # ends the loop
    print 'are you today?'