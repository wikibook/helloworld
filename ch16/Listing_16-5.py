# Listing_16-5.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Draw a circle in the middle of the window

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])

# draw circle in the middle of the Pygame window
pygame.draw.circle(screen, [255,0,0],[320,240], 30, 0)    # [320,240] is the new location   
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()