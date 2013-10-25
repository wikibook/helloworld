# Listing_8-9.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Using continue in a loop

for i in range (1, 6):
    print
    print 'i =', i,
    print 'Hello, how',
    if i == 3:
        continue              # ends current iteration of the loop
    print 'are you today?'