from random import *
import javarandom as jr


javaRandom = jr.Random()

class RDSItem:
    'represents an item in a pool'

    def __init__(
            self,
            rdsName:str,
            rdsStackSize:tuple(),
            rdsWeight:tuple()
    ):
        self.setrdsName(rdsName)
        self.setrdsStackSize(rdsStackSize)
        self.setrdsWeight(rdsWeight)
    
    def setrdsName(
            self,
            rdsName:str
    ):
        self.rdsName = rdsName
    
    def getrdsName(self):
        return self.rdsName

    def setrdsStackSize(
            self,
            rdsStackSize:tuple()
    ):
        self.rdsStackSize = rdsStackSize
    
    def getrdsStackSize(self):
        return self.rdsStackSize
    
    def setrdsWeight(
            self,
            rdsWeight:tuple()
    ):
        self.rdsWeight = rdsWeight
    
    def getrdsWeight(self):
        return self.rdsWeight
    
    def getAttr(self):
        return (self.getrdsStackSize,self.getrdsWeight)


class RDSPool:
    'represents a pool of loot'

    def __init__(
            self,
            rdsDraws:tuple(),
            pool_name:str = None
    ):
        self.setrdsDraws(rdsDraws)
        self.rdsItems = []
        self.setPoolName(pool_name)

    def setrdsDraws(
            self,
            rdsDraws:tuple()
    ):
        self.rdsDraws = rdsDraws

    def setPoolName(self,pool_name):
        self.pool_name = pool_name
    
    def getrdsDraws(self):
        return self.rdsDraws
    
    def getPoolName(self):
        return self.pool_name

    def addItem(
            self,
            item:RDSItem
    ):
        self.rdsItems.append(item)

    def removeItem(
            self
    ):
        pass
    
    def getItems(
            self
    ):
        return self.rdsItems
    
    def getItem(
            self,
            rdsItemName:str
    ):
        for item in self.getItems():
            if rdsItemName == item.getrdsName():
                return item
    
    def __str__(self):
        if self.getPoolName() != None:
            return self.getPoolName()
        else:
            return f"<loot_table_generator.RDSPool at {hex(id(self))}>"
    
    def __repr__(self):
        return self.__str__()


class RDSTable:
    'represents a table of loot pools'

    def __init__(self):
        self.rdsPools = []
    
    def generate(self):
        result = {}
        for pool in self.rdsPools:
            probabilityList = []
            for item in pool.rdsItems:
                probabilityList.extend(
                    [item.getrdsName()]*item.getrdsWeight()[0])
            # print(f'Probability List: {probabilityList}')
            drawRoll = javaRandom.nextInt(pool.getrdsDraws()[1]-pool.getrdsDraws()[0]+1) + pool.getrdsDraws()[0]
            # print(f'Draw Roll: {drawRoll} ({pool.getrdsDraws()[0]},{pool.getrdsDraws()[1]})')
            for _ in range(drawRoll):
                itemPickedName = probabilityList[javaRandom.nextInt(len(probabilityList))]
                # print(f'Item Picked: {itemPickedName},', end=' ')
                itemPickedStackSize = javaRandom.nextInt(
                    pool.getItem(itemPickedName).getrdsStackSize()[1]-pool.getItem(itemPickedName).getrdsStackSize()[0]+1
                )+pool.getItem(itemPickedName).getrdsStackSize()[0]
                # print(f'Item Count: {itemPickedStackSize} ({pool.getItem(itemPickedName).getrdsStackSize()[0]}/{pool.getItem(itemPickedName).getrdsStackSize()[1]})')
                if itemPickedName in result:
                    result[itemPickedName] += itemPickedStackSize
                    # print(f'Current Results: {result}')
                else:
                    result.update({itemPickedName:itemPickedStackSize})
                    # print(f'Current Results: {result}')
        return result
    
    def drop(
            self,
            rdsDraws:int
    ):
        result = {}
        for _ in range(rdsDraws):
            probabilityList = []
            for item in self.getPools()[0].getItems():
                probabilityList.extend(
                    [item.getrdsName()]*item.getrdsWeight()[0])
            # print(f'Probability List: {probabilityList}')
            itemPickedName = probabilityList[javaRandom.nextInt(len(probabilityList))]
            # print(f'Item Picked: {itemPickedName},', end=' ')
            itemPickedStackSize = javaRandom.nextInt(
                    self.getPools()[0].getItem(itemPickedName).getrdsStackSize()[1] - self.getPools()[0].getItem(itemPickedName).getrdsStackSize()[0] + 1
                ) + self.getPools()[0].getItem(itemPickedName).getrdsStackSize()[0]
            # print(f'Item Count: {itemPickedStackSize} ({pool.getItem(itemPickedName).getrdsStackSize()[0]}/{pool.getItem(itemPickedName).getrdsStackSize()[1]})')
            if itemPickedName in result:
                result[itemPickedName] += itemPickedStackSize
                # print(f'Current Results: {result}')
            else:
                result.update({itemPickedName:itemPickedStackSize})
                # print(f'Current Results: {result}')
        return result
            
    def addPool(
            self,
            pool:RDSPool
    ):
        self.rdsPools.append(pool)
    
    def removePool(
            self
    ):
        pass
    
    def getPools(self):
        return self.rdsPools