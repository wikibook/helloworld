# Listing_22-5.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Using 'w' mode on an existing file

the_file = open('notes.txt', 'w')
the_file.write("Wake up\n")
the_file.write("Watch cartoons")
the_file.close()
