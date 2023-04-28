# EVENTS: https://www.tutorialspoint.com/pygame/pygame_event_objects.htm


import sys
import pygame as pg
from pygame.locals import *
pg.init()



SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pg.RESIZABLE)
pg.display.set_caption("Inventory Trainer")

screen.fill((255,255,255))

run = True
while run:
    
    pg.display.update()

    for event in pg.event.get():
        # Close window button
        if event.type == QUIT:
            run = False
        # Mouse hold/click
        if event.type == MOUSEBUTTONDOWN:
            pos=pg.mouse.get_pos()
            btn=pg.mouse
            print("x = {}, y = {}".format(pos[0], pos[1]))
        # Mouse movement
        if event.type == MOUSEMOTION:
            pos=event.pos
            print ("x = {}, y = {}".format(pos[0], pos[1]))
        # Key Press
        if event.type == KEYDOWN:
            key = pg.key.name(event.key)
            print(key, 'is pressed')
        if event.type == KEYUP:
            key = pg.key.name(event.key)
            print(key, 'is released')

pg.quit()
sys.exit(1)