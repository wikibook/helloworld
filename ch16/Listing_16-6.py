# Listing_16-6.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Make "modern art" by drawing random rectangles

import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
for i in range (100):
    #pick random numbers for rectangle size and position
    width = random.randint(0, 250)
    height = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)
    
    # draw the rectangle
    pygame.draw.rect(screen, [0,0,0], [left, top, width, height], 1)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()