import pygame as pg
import sys

pg.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


run = True
while run:
    
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run == False


pg.quit()
sys.exit()