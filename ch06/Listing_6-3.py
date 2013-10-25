# Listing_6-3.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# easygui text box

import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",)
easygui.msgbox ("You entered " + flavor)