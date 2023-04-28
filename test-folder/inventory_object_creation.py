speedrunItemsFileDirectory = 'assets/text-files/speedrun_items.txt'



class Grid:
    'represents a container of items in a grid'

    def __init__(self,rows:int = 1,columns:int = 1):
        self.__setRows(rows)
        self.__setColumns(columns)
        self.__items = [[None for ir in range(self.getRows())] for ic in range(self.getColumns())]
        
    def __setRows(self,rows:int):
        self.__rows = rows

    def __setColumns(self,columns:int):
        self.__columns = columns
                  
    def setItem(self,value,x:int,y:int):
        if 0<=x<=self.getColumns() and 0<=y<=self.getRows():
            self.__items[x][y] = value
        else:
            raise IndexError(f'''
            
Index(es) out of range for {self}:
Max values accepted are x = {self.getColumns()}, y = {self.getRows()}
Values also must be greater than or equal to 0.''')
                  
    def switchItems(self,x1,y1,x2,y2):
        if 0<=x1<self.getColumns() and 0<=y1<=self.getRows() and\
          0<=x2<self.getColumns() and 0<=y2<=self.getRows():
            self.__items[x1][y1],self.__items[x2][y2] = self.__items[x2][y2],\
                                                        self.__items[x1][y1]
        else:
            raise IndexError(f'''

Index(es) out of range for {self}:
Max values accepted are x = {self.getColumns()}, y = {self.getRows()}
Values also must be greater than or equal to 0.''')

    def getRows(self):
        return self.__rows

    def getColumns(self):
        return self.__columns
    
    def getItem(self,x:int,y:int):
        if 0<=x<=self.getColumns() and 0<=y<=self.getRows():
            return self.__items[x][y]
        else:
            raise IndexError(f'''

Index(es) out of range for {self}:
Max values accepted are x = {self.getColumns()}, y = {self.getRows()}
Values also must be greater than or equal to 0.''')

    def getItems(self):
        return self.__items
    
    def getID(self,x,y):
        if 0<=x<=self.getColumns() and 0<=y<=self.getRows():
            if self.__items[x][y] != None:
                return Item.getID(self.__items[x][y])
            else:
                raise LookupError(f'\n\nNo item found at {x},{y}')
        else:
            raise IndexError(f'''

Index(es) out of range for {self}:
Max values accepted are x = {self.getColumns()}, y = {self.getRows()}
Values also must be greater than or equal to 0.''')
                  
    def getCount(self,x,y):
        if 0<=x<=self.getColumns() and 0<=y<=self.getRows():
            if self.__items[x][y] != None:
                return Item.getCount(self.__items[x][y])
            else:
                raise LookupError(f'\n\nNo item found at {x},{y}')
        else:
            raise IndexError(f'''
            
Index(es) out of range for {self}:
Max values accepted are x = {self.getColumns()}, y = {self.getRows()}
Values also must be greater than or equal to 0.''')
                  
    def printItem(self,x,y):
        if 0<=x<=self.getColumns() and 0<=y<=self.getRows():
            if self.__items[x][y] != None:
                print(f'ID: {Item.getID(self.__items[x][y])}, Count: {Item.getCount(self.__items[x][y])}')
            else:
                print(None)
        else:
            raise IndexError(f'''
            
Index(es) out of range for {self}:
Max values accepted are x = {self.getColumns()}, y = {self.getRows()}
Values also must be greater than or equal to 0.''')

    def printItems(self):
        for iy in range(len(self.__items[0])):
            print()
            for ix in range(len(self.__items)):
                if self.__items[ix][iy] != None:
                    stringy = f'{Item.getID(self.__items[ix][iy])}:{Item.getCount(self.__items[ix][iy])}'
                    print('{: <16}'.format(stringy),end='')
                else:
                    print(None,end='\t\t')

class Inventory:
    'represents an inventory container'

    def __init__(self,rows: int = 0,columns: int = 0,inv_type: str = 'inventory'):
        self.__container = Grid(rows,columns)
        self.__inv_type = inv_type
        self.__rows = rows
        self.__columns = columns

    def addItem(self, id:str, count:int, x:int, y:int):
        if self.__container.getItem(x,y) == None:
            try:
                self.__container.setItem(Item(id,count),x,y)
            except:
                pass
        else:
            raise ValueError(f'Item {Item.getID(self.__container.getItem(x,y))}:{Item.getCount(self.__container.getItem(x,y))} exists at position {x},{y}')
        
    def quickAddItem(self,id:str, count:int):
        for iy in range(self.getColumns()):
            for ix in range(self.getRows()):
                try:
                    if self.__container.getItem(ix,iy) != None:
                        continue
                    else:
                        self.__container.setItem(Item(id,count),ix,iy)
                        return
                except:
                    return

    def getItem(self,x:int,y:int):
        if 0<=x<=self.getColumns() and 0<=y<=self.getRows():
            return self.__container.getItem(x,y)
        else:
            raise IndexError(f'''
            
Index(es) out of range for {self}:
Max values accepted are x = {self.getColumns()}, y = {self.getRows()}
Values also must be greater than or equal to 0.''')

    def getType(self) -> str:
        return self.__inv_type
    
    def getRows(self) -> int:
        return self.__rows
    
    def getColumns(self) -> int:
        return self.__columns
    
    def getAttr(self):
        return (self.__inv_type,self.__rows,self.__columns)
    
    def printItems(self):
        self.__container.printItems()

class Item:
    'represents an item'

    speedrunItemsFile = open(speedrunItemsFileDirectory,'r')
    itemPool = speedrunItemsFile.readlines()
    for i in range(len(itemPool)):
        itemPool[i] = itemPool[i][:-1]
    itemPool = set(itemPool)
    speedrunItemsFile.close()

    def __init__(self,id: str = 'sweet_berries',count: int = 1):
        self.setID(id)
        self.setCount(count)

    def setID(self,id: str) -> None:
        if id in Item.itemPool:
            self.__id = id
        else:
            raise ValueError(f'\n\n{id} is not a vaid item.')
    
    def setCount(self,count: int) -> None:
        if count <= 64:
            self.__count = count
        else:
            raise ValueError(f'{count} is too large. Value must be 64 or lower.')
    
    def setAttr(self,id: str,count: int) -> None:
        self.setID(id)
        self.setCount(count)
    
    def getID(self) -> str:
        return self.__id
    
    def getCount(self) -> int:
        return self.__count
    
    def getAttr(self):
        return (self.__id,self.__count)





armorInventory = Inventory(4,1,'armor')
armorInventory.addItem('golden_helmet',1,0,0)
armorInventory.addItem('iron_chestplate',1,0,1)
armorInventory.addItem('iron_leggings',1,0,2)
armorInventory.addItem('iron_boots',1,0,3)
armorInventory.printItems()

print('\n'+'_'*20)

mainInventory = Inventory(3,9,'main')
mainInventory.addItem('bread',64,3,2)
mainInventory.quickAddItem('oak_door',3)
mainInventory.quickAddItem('oak_boat',1)
mainInventory.printItems()

print('\n'+'_'*20)

hotbarInventory = Inventory(1,9,'hotbar')
hotbarInventory.addItem('bread',17,3,0)
hotbarInventory.addItem('stone_axe',1,0,0)
hotbarInventory.addItem('iron_pickaxe',1,1,0)
# hotbarInventory.addItem('stone_shovel',1,1,0)   ValueError: Item stone_pickeaxe:1 exists at position 1,0
hotbarInventory.addItem('diamond_shovel',1,2,0)
hotbarInventory.addItem('oak_boat',1,4,0)
hotbarInventory.addItem('water_bucket',1,5,0)
hotbarInventory.addItem('flint_and_steel',1,6,0)
hotbarInventory.addItem('lava_bucket',1,7,0)
hotbarInventory.addItem('iron_ingot',2,8,0)
hotbarInventory.quickAddItem('apple',2)
hotbarInventory.printItems()