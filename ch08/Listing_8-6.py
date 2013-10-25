# Listing_8-6
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Countdown timer

import time
for i in range (10, 0, -1):         # count backwards
    print i
    time.sleep(1)                   # wait one second
print "BLAST OFF!"