# Listing_5-3.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Temperature conversion using raw_input()

print "This program converts Fahrenheit to Celsius"
print "Type in a temperature in Fahrenheit: ",

# Use int(raw_input()) to get the Fahrenheit temperature from the user
fahrenheit = float(raw_input())

celsius = (fahrenheit - 32) * 5.0 / 9
print "That is",                           # Notice the commas                   
print celsius,                             # at the and of these lines                 
print "degrees Celsius"
