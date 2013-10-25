# Listing_16-3.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Making the Pygame window closeable

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
while True:
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:      # now we can get out
            sys.exit()                     #  of the endless loop