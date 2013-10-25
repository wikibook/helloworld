# Listing_5-4.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Getting input from a file on the web

import urllib
file = urllib.urlopen('http://helloworldbook.com/data/message.txt')
message = file.read() 
print message

