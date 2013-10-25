# TIO_CH22_2.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Save some data to a text file

name = raw_input("Enter your name: ")
age = raw_input("Enter your age: ")
color = raw_input("Enter your favorite color: ")
food = raw_input("Enter your favorite food: ")

my_data = open("my_data_file.txt", 'w')

my_data.write(name + "\n")
my_data.write(age + "\n")
my_data.write(color + "\n")
my_data.write(food)

my_data.close()
