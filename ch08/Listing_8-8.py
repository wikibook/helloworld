# Listing_8-8.py  
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# A conditional or while loop
print "Type 3 to continue, anything else to quit."
someInput = raw_input()
while someInput == '3':                                  # loop condition
    print "Thank you for the 3.  Very kind of you."          #  body
    print "Type 3 to continue, anything else to quit."       #  of the 
    someInput = raw_input()                                  #  loop
print "That's not 3, so I'm quitting now."