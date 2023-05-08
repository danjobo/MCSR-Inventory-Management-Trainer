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
mouseMode = 'hover'


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
            if apple.rect.collidepoint(*mousePos) and not apple.clicked and mouseMode == 'hover':
                apple.clicked = True
                mouseMode = 'drag'
            elif mouseMode == 'drag' and apple.clicked:
                apple.clicked = False
                mouseMode = 'hover'
        if event.type == MOUSEBUTTONUP:
            mousePos=pg.mouse.get_pos()  # a tuple
            # btn=pg.mouse
            mouseDown = False
        # Mouse movement
        if event.type == MOUSEMOTION:
            mousePos=event.pos # a tuple
        # Key Press
        if event.type == KEYDOWN:
            keyDown = pg.key.name(event.key)
        if event.type == KEYUP:
            keyUp = pg.key.name(event.key)



    # Collision Detection
    # if apple.rect.collidepoint(*mousePos) and clicked and mouseMode == 'hover' and not apple.clicked:
    #     apple.clicked = True
    #     mouseMode = 'drag'
    # elif clicked and mouseMode == 'drag' and apple.clicked:
    #     apple.clicked = False
    #     mouseMode = 'hover'
    

    if apple.clicked and mouseMode == 'drag':
        apple.centerOn(mousePos[0],mousePos[1])


    # RENDER GAME HERE
    screen.blit(background,screenRect)
    UI_ELEMENTS_GROUP.draw(screen)
    ITEMS_GROUP.draw(screen)


    # Info Print