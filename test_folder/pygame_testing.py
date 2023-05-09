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
mousePos = (0,0) 
mouseDown = False
mouseMode = 'hover'
clicked = None


# Sprites
background = pg.image.load('./assets/misc/background1.jpg')


ITEMS_GROUP = pg.sprite.Group()
apple = Item('./assets/items/apple.png',287,27)
iron_ingot = Item('./assets/items/iron_ingot.png',350,27)
ITEMS_GROUP.add(apple,iron_ingot)


CLICKED_ITEMS_GROUP = pg.sprite.Group()


UI_ELEMENTS_GROUP = pg.sprite.Group()
inventory = UIElement('./assets/misc/inventory-snip.png',287,27)
UI_ELEMENTS_GROUP.add(inventory)



# Additional Variables
item_drag_switch_case_dict = {}
for sprite in ITEMS_GROUP.spritedict:
    item_drag_switch_case_dict.update({str(sprite):sprite.centerOn})



# Main Loop
while True:

    # Sets FPS to 60
    clock.tick(FPS)

    # Makes it work on your screen
    pg.display.flip()



    # Event Loop
    for event in pg.event.get():
        match event.type:
            case 256: # QUIT
                pg.quit()
                sys.exit(1)
            case 1025: # MOUSEBUTTONDOWN
                if event.button == 1:
                    mousePos=pg.mouse.get_pos()  # a tuple
                    # btn=pg.mouse      # mouse module??
                    mouseDown = True
                    # Item Collision Detection
                    for item in ITEMS_GROUP.spritedict:
                        if item.rect.collidepoint(*mousePos) and not item.clicked and mouseMode == 'hover':
                            item.clicked = True
                            clicked = item
                            mouseMode = 'drag'
                            CLICKED_ITEMS_GROUP.add(item)
                        elif mouseMode == 'drag' and item.clicked:
                            item.clicked = False
                            clicked = None
                            mouseMode = 'hover'
                            CLICKED_ITEMS_GROUP.remove(item)
                            # for item2 in ITEMS_GROUP.spritedict:
                            #     if item2.rect.collidepoint(*mousePos) and not item2.clicked and mouseMode == 'hover':
                            #         item2.clicked = True
                            #         clicked = item2
                            #         mouseMode = 'drag'
                            #     elif mouseMode == 'drag' and item2.clicked:
                            #         item2.clicked = False
                            #         clicked = None
                            #         mouseMode = 'hover'
                    
            case 1026: # MOUSEBUTTONUP
                mousePos=pg.mouse.get_pos()  # a tuple
                # btn=pg.mouse
                mouseDown = False
            case 1024: # MOUSEMOTION
                mousePos=event.pos # a tuple
            case 768: # KEYDOWN
                keyDown = pg.key.name(event.key)
            case 769: # KEYUP
                keyUp = pg.key.name(event.key)
            case _:
                pass



    # Collision Detection


    
    # COMPUTATION
    
    # Makeshift Switch Statement for Item Movement w/ Mouse
    # if clicked == None:
    #     pass
    # else:
    #     item_drag_switch_case_dict[str(clicked)](*mousePos)

    if isinstance(clicked,Item):
        item_drag_switch_case_dict[str(clicked)](*mousePos)

    


    # RENDER GAME HERE
    screen.blit(background,screenRect)
    UI_ELEMENTS_GROUP.draw(screen)
    ITEMS_GROUP.draw(screen)
    CLICKED_ITEMS_GROUP.draw(screen)


    # Debug Info Print