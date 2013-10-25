# TIO_CH21_3.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Calculate all the fractions of 8 and display them
#   with 3 decimal places

for i in range(1, 9):
    fraction = i / 8.0
    print str(i) + '/8 = %.3f' % fraction
    