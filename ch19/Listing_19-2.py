# Listing_19-2.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Playing music

import pygame, sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load("bg_music.mp3")               
pygame.mixer.music.play()                             

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()