# Listing_22-2.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Using readline() more than once

my_file   = open('notes.txt', 'r')
first_line = my_file.readline()
second_line = my_file.readline()
print "first line = ", first_line
print "second line = ", second_line
my_file.close()
