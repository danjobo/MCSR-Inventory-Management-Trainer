import pygame as pg


class RenderObject:
    'represents a rendered object on the screen'

    def __init__(self, image:pg.surface.Surface, x:int=0, y:int=0):
        ''
        self.setImage(image)
        self.setX(x)
        self.sety(y)
    
    def setImage(self, image):
        ''
        self.image == image

    def setX(self, x):
        ''
        self.x = x
        
    
    def setY(self, y):
        ''
        self.y = y

    def getImage(self):
        ''
        return self.image

    def getX(self):
        ''
        return self.x
    
    def getY(self):
        ''
        return self.y
    

