# EVENTS: https://www.tutorialspoint.com/pygame/pygame_event_objects.htm
import sys,pygame as pg
from additional_classes import *
from pygame.locals import *

# General Setup
pg.init()
clock = pg.time.Clock()
FPS = 60


# App Window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pg.RESIZABLE)
screenRect = screen.get_rect()
pg.display.set_caption('ItemBot')
pg.display.set_icon(pg.image.load('./assets/misc/end_crystal_icon_Tde_icon.ico'))



# Event Variables
mousePos = (0,0) 
mouseDown = False


# Sprites
background = pg.image.load('./assets/misc/background1.jpg')


ITEMS_GROUP = pg.sprite.Group()

apple = Item('./assets/items/apple.png',287,27)
ITEMS_GROUP.add(apple)

UI_ELEMENTS_GROUP = pg.sprite.Group()

inventory = UIElement('./assets/misc/inventory-snip.png',287,27)
UI_ELEMENTS_GROUP.add(inventory)








# Main Loop
while True:

    # Sets FPS to 60
    clock.tick(FPS)

    # Makes it work on your screen
    pg.display.flip()



    # Event Loop
    for event in pg.event.get():
        # Close window button
        if event.type == QUIT:
            pg.quit()
            sys.exit(1)
        # Mouse hold/click
        if event.type == MOUSEBUTTONDOWN:
            mousePos=pg.mouse.get_pos()  # a tuple
            # btn=pg.mouse      # mouse module??
            mouseDown = True
        if event.type == MOUSEBUTTONUP:
            mousePos=pg.mouse.get_pos()  # a tuple
            # btn=pg.mouse
            mouseDown = False
        # Mouse movement
        if event.type == MOUSEMOTION:
            mousePos=event.pos # a tuple
        # Key Press
        if event.type == KEYDOWN:
            # if event.key == K_RIGHT:
            #     invX += 5
            # if event.key == K_LEFT:
            #     invX -= 5
            # if event.key == K_UP:
            #     invY -= 5
            # if event.key == K_DOWN:
            #     invY += 5
            keyDown = pg.key.name(event.key)
        if event.type == KEYUP:
            keyUp = pg.key.name(event.key)



    # Collision Detection
    if apple.rect.collidepoint(mousePos[0],mousePos[1]) and mouseDown:
        apple.mouseDown = True
    
    if apple.mouseDown == True:
        apple.centerOn(mousePos[0],mousePos[1])


    # RENDER GAME HERE
    screen.blit(background,screenRect)
    UI_ELEMENTS_GROUP.draw(screen)
    ITEMS_GROUP.draw(screen)