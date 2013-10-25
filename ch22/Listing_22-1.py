# Listing_22-1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Opening and reading from a file

my_file = open('notes.txt', 'r')
lines = my_file.readlines()
print lines
