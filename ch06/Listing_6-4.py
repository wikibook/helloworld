# Listing_6-4.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# default arguments in easygui

import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                           default = 'Vanilla')     # here's the default
easygui.msgbox ("You entered " + flavor)