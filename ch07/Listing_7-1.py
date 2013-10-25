# Listing_7-1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Try some comparisons using relational operators

num1 = float(raw_input("Enter the first number: "))
num2 = float(raw_input("Enter the second number: "))
if num1 < num2:
    print num1, "is less than", num2
if num1 > num2:
    print num1, "is greater than", num2
if num1 == num2:                                
    print num1, "is equal to", num2
if num1 != num2:
    print num1, "is not equal to", num2
