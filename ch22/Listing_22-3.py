# Listing_22-3.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Using append mode

todo_list = open('notes.txt', 'a')
todo_list.write('\nSpend allowance')
todo_list.close()                                                         
