import pygame as pg

class GameWindow:
    ''

    def __init__(
            self,
            active=False,
            *renderobjects
        ):
        ''
        self.setActive(active)
        self.objectDict = {}
        for renderobject in renderobjects:
            self.addRenderObject(renderobject)

    def validConstructor(self,argument, constructor):
        try:
            constructor(argument)
            return True
        except:
            return False


    def setActive(self,active):
        ''
        self.active = active

    def addRenderObject(self,renderobj):
        if str(type(renderobj)).split('.')[1].rstrip("'>") == 'RenderObject':
            if renderobj.getName() != None:
                self.objectDict.update({renderobj.getName():renderobj})
            else:
                self.objectDict.update({str(renderobj):renderobj})
    
    def getActive(self):
        ''
        return self.active
    
    def getRenderObjects(self):
        return self.objectDict
    
    def getRenderObject(
            self, 
            name:str = None,
            id:str = None
        ):
        ''
        if name == None and id != None:
            if self.validConstructor(id,int):
                return self.objectDict[id]
        elif id == None and name != None:
            if not self.validConstructor(name,int):
                return self.objectDict[name]
        else:
            raise KeyError('No Key Provided')
    


class RenderObject:
    'represents a rendered object on the screen'

    def __init__(
            self, 
            image:pg.surface.Surface, 
            x:int=0, 
            y:int=0, 
            name:str=None, 
            hidden=False
        ):
        ''
        self.setImage(image)
        self.setX(x)
        self.setY(y)
        self.setName(name)
        self.setHidden(hidden)
    
    def setImage(self, image):
        ''
        self.__image = image

    def setX(self, x):
        ''
        self.x = x
        
    
    def setY(self, y):
        ''
        self.y = y

    def setName(self, name:str):
        ''
        self.name = name

    def setHidden(self,hidden):
        ''
        self.hidden = hidden

    def getImage(self):
        ''
        return self.__image

    def getX(self):
        ''
        return self.x
    
    def getY(self):
        ''
        return self.y
    
    def getName(self):
        ''
        return self.name
    
    def getHidden(self):
        ''
        return self.hidden
    
    def __str__(self):
        ''
        return hex(id(self))


if __name__ == "__main__":
    playButton = RenderObject('play',0,0)
    settingsButton = RenderObject('gear',0,0)
    mainMenu = GameWindow(
        True,
        playButton,
        settingsButton,
        RenderObject(
            'apple',
            0,
            0,
            'optionsButton'
        ),
        RenderObject(
            'title',
            0,
            0
        )
    )
    print(mainMenu.getRenderObjects())
    print(mainMenu.getRenderObject(id=str(playButton)))
    print(str(playButton))
    print(mainMenu.objectDict[str(playButton)])
    print(mainMenu.validConstructor(hex(id(playButton)),int))