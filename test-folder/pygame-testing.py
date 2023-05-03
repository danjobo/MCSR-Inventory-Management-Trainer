# EVENTS: https://www.tutorialspoint.com/pygame/pygame_event_objects.htm


import sys
import pygame as pg
from additional_classes import *
from pygame.locals import *
pg.init()



SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pg.RESIZABLE)
pg.display.set_caption("Inventory Trainer")

clock = pg.time.Clock()


inventoryBG = pg.image.load('./assets/misc/inventory-snip.png')
inventoryRect = inventoryBG.get_rect()
invX, invY = 287, 27



running = True
while running:
    mouseX, mouseY = pg.mouse.get_pos()

    screen.fill((255,255,255))

    for event in pg.event.get():
        # Close window button
        if event.type == QUIT:
            running = False
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
            if event.key == K_RIGHT:
                invX += 5
            if event.key == K_LEFT:
                invX -= 5
            if event.key == K_UP:
                invY -= 5
            if event.key == K_DOWN:
                invY += 5
            key = pg.key.name(event.key)
            print(key, 'is pressed')
        if event.type == KEYUP:
            key = pg.key.name(event.key)
            print(key, 'is released')


    # RENDER GAME HERE
    inventoryRect.topleft = invX, invY
    screen.blit(inventoryBG, inventoryRect)


    # Makes it work on your screen
    pg.display.flip()
    
    # Sets FPS to 60
    clock.tick(60)

pg.display.update()
pg.quit()
sys.exit(1)