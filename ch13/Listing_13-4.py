# Listing_13-4
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Creating and using a function that returns a value

# Function to calculate tax and return the total
def calculateTax(price, tax_rate):                       
    total = price + (price * tax_rate)                   
    return total                          # return the total              

my_price = float(raw_input ("Enter a price: "))          

# Call the function and store the result in totalPrice
totalPrice = calculateTax(my_price, 0.06) 
               
print "price = ", my_price, " Total price = ", totalPrice