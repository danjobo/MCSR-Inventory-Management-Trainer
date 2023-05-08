import pygame as pg
    
class UIElement(pg.sprite.Sprite):
    'Create a UI Element'
    def __init__(
            self,
            filepath:str,
            pos_x:float = 0,
            pos_y:float = 0
    ):
        super().__init__()
        self.image = pg.image.load(filepath)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x,pos_y)
        self.movex = 0
        self.movey = 0
    
    def centerOn(self,pos_x,pos_y):
        self.rect.center = (pos_x,pos_y)

    def move(self, deltaX, deltaY):
        'control item movement'
        self.movex += deltaX
        self.movey += deltaY
    
    def position(self,pos_x,pos_y):
        self.rect.topleft = (pos_x,pos_y)

    def update(self):
        'update sprite position'
        self.rect.x 

class Item(pg.sprite.Sprite):
    'Spawn an item'
    def __init__(
            self,
            filepath:str,
            pos_x:float = 0,
            pos_y:float = 0
    ):
        super().__init__()
        self.image = pg.image.load(filepath)
        self.image = pg.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x,pos_y)
        self.mouseDown = False

    def centerOn(self,pos_x,pos_y):
        'Sets an items position centered on a given x and y coordinate'
        self.rect.center = (pos_x,pos_y)

    def getImage(self):
        ''
        return self.image
    
    def getRect(self):
        ''
        return self.rect
    
    def position(self,pos_x,pos_y):
        '''Sets a an items position with it\'s top left corner at a
given x and y coordinate'''
        self.rect.topleft = (pos_x,pos_y)

    def scale(self,width,height,dest_surface=None):
        ''
        self.image = pg.transform.scale(self.image,(width,height),dest_surface)
        self.rect = self.image.get_rect()


if __name__ == "__main__":
    pass