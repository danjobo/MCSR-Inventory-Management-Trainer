# EVENTS: https://www.tutorialspoint.com/pygame/pygame_event_objects.htm
import sys,pygame as pg
from additional_classes import *
from functions import *
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
null = None
mousePos = (0,0) 
mouseDown = False
mouseMode = 'hover'
clicked = null


# Sprites
background = pg.image.load('./assets/misc/background1.jpg')


ITEMS_GROUP = pg.sprite.Group()
apple = Item('./assets/items/apple.png',287,27)
iron_ingot = Item('./assets/items/iron_ingot.png',350,27)
ITEMS_GROUP.add(apple,iron_ingot)


UI_ELEMENTS_GROUP = pg.sprite.Group()
inventory = UIElement('./assets/misc/inventory-snip.png',287,27)
UI_ELEMENTS_GROUP.add(inventory)



# Additional Variables
item_movement_dict = {}
for sprite in ITEMS_GROUP.spritedict:
    item_movement_dict.update({str(sprite):sprite.centerOn})



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
            if event.button == 1:
                mousePos=pg.mouse.get_pos()  # a tuple
                # btn=pg.mouse      # mouse module??
                mouseDown = True
                if apple.rect.collidepoint(*mousePos) and not apple.clicked and mouseMode == 'hover':
                    apple.clicked = True
                    clicked = apple
                    mouseMode = 'drag'
                elif mouseMode == 'drag' and apple.clicked:
                    apple.clicked = False
                    clicked = null
                    mouseMode = 'hover'
                if iron_ingot.rect.collidepoint(*mousePos) and not iron_ingot.clicked and mouseMode == 'hover':
                    iron_ingot.clicked = True
                    clicked = iron_ingot
                    mouseMode = 'drag'
                elif mouseMode == 'drag' and iron_ingot.clicked:
                    iron_ingot.clicked = False
                    clicked = None
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


    
    # Computation
    
    # Makeshift Switch Statement for Item Movement w/ Mouse
    if clicked == None:
        pass
    else:
        item_movement_dict[str(clicked)](*mousePos)

    


    # RENDER GAME HERE
    screen.blit(background,screenRect)
    UI_ELEMENTS_GROUP.draw(screen)
    ITEMS_GROUP.draw(screen)


    # Info Print