# Listing_19-1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Trying out sounds in Pygame

import pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

splat = pygame.mixer.Sound("splat.wav")
splat.play()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()