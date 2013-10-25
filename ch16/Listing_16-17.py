# Listing_16-17.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# move a beach ball image in a pygame window with wrapping

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('beach_ball.png')
x = 50
y = 50
x_speed = 5
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255,255,255], [x, y, 90, 90], 0)
    x = x + x_speed
    if x > screen.get_width():                                
        x = 0                                                  
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
