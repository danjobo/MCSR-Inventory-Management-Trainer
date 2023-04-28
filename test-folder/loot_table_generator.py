from random import *
import javarandom as jr

# Output: A dictionary containing all items found with the name as the key and the total found as the value

# Input
# buriedTreasure = RDSTable(args...).
# print(buriedTreasure.generate())

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
            rdsDraws:tuple()
    ):
        self.setrdsDraws(rdsDraws)
        self.rdsItems = []

    def setrdsDraws(
            self,
            rdsDraws:tuple()
    ):
        self.rdsDraws = rdsDraws
    
    def getrdsDraws(self):
        return self.rdsDraws
    
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







# buriedTreasure = RDSTable()
# buriedTreasure.addPool(RDSPool((1,1)))

# RDSPool.addItem(buriedTreasure.getPools()[0],RDSItem(
#     'heart_of_the_sea',
#     (1,1),
#     (1/1)
#     ))

# print(RDSItem.getrdsName(RDSPool.getItems(buriedTreasure.getPools()[0])[0]))

# print(buriedTreasure.getPools()[0].getItems()[0].getrdsName())



buriedTreasure = RDSTable()



# Underwater Pool
buriedTreasure.addPool(RDSPool((1,1)))
buriedTreasure.getPools()[0].addItem(RDSItem(
    'heart_of_the_sea',
    (1,1),
    (1,1)
    ))

# Useful Pool
buriedTreasure.addPool(RDSPool((5,8)))
buriedTreasure.getPools()[1].addItem(RDSItem(
    'iron_ingot',
    (1,4),
    (20,35)
    ))
buriedTreasure.getPools()[1].addItem(RDSItem(
    'gold_ingot',
    (1,4),
    (10,35)
    ))
buriedTreasure.getPools()[1].addItem(RDSItem(
    'tnt',
    (1,2),
    (5,35)
    ))

# Rare Pool
buriedTreasure.addPool(RDSPool((1,4)))
buriedTreasure.getPools()[2].addItem(RDSItem(
    'emerald',
    (4,8),
    (5,15)
    ))
buriedTreasure.getPools()[2].addItem(RDSItem(
    'prismarine_crystals',
    (1,5),
    (5,15)
    ))
buriedTreasure.getPools()[2].addItem(RDSItem(
    'diamond',
    (1,2),
    (5,15)
    ))

# Equipment Pool
buriedTreasure.addPool(RDSPool((0,1)))
buriedTreasure.getPools()[3].addItem(RDSItem(
    'leather_chestplate',
    (1,1),
    (1,2)
    ))
buriedTreasure.getPools()[3].addItem(RDSItem(
    'iron_sword',
    (1,1),
    (1,2)
    ))

# Food Pool
buriedTreasure.addPool(RDSPool((2,2)))
buriedTreasure.getPools()[4].addItem(RDSItem(
    'cooked_cod',
    (2,4),
    (1,2)
    ))
buriedTreasure.getPools()[4].addItem(RDSItem(
    'cooked_salmon',
    (2,4),
    (1,2)
    ))

# Potion Pool
buriedTreasure.addPool(RDSPool((0,2)))
buriedTreasure.getPools()[5].addItem(RDSItem(
    'potion_of_water_breathing',
    (1,1),
    (1,1)
    ))

# i = 0
# for pool in buriedTreasure.getPools():
#     i += 1
#     print(f'Pool {i}')
#     for item in pool.getItems():
#         print(item.getrdsName())


# print(buriedTreasure.generate())

for k,v in buriedTreasure.generate().items():
    print(f'{k: <18}: {v}')


# Would be easier to access pools if you could acces them by name, like a dictionary


piglinBartering = RDSTable()



# Main Pool
piglinBartering.addPool(RDSPool((1,1)))
piglinBartering.getPools()[0].addItem(RDSItem(
    'enchanted_book',
    (1,1),
    (5,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'iron_boots',
    (1,1),
    (8,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'splash_potion_of_fire_resistance',
    (1,1),
    (8,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'potion_of_fire_resistance',
    (1,1),
    (8,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'water_botle',
    (1,1),
    (10,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'iron_nugget',
    (10,36),
    (10,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'ender_pearl',
    (2,4),
    (510,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'string',
    (3,9),
    (20,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'nether_quartz',
    (5,12),
    (20,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'obsidian',
    (1,1),
    (40,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'crying_obsidian',
    (1,3),
    (40,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'fire_charge',
    (1,1),
    (40,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'leather',
    (2,4),
    (40,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'soul_sand',
    (2,8),
    (40,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'nether_brick',
    (2,8),
    (40,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'spectral_arrow',
    (6,12),
    (40,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'gravel',
    (8,16),
    (40,459)
    ))
piglinBartering.getPools()[0].addItem(RDSItem(
    'blackstone',
    (8,16),
    (40,459)
    ))


# print(piglinBartering.drop(5))

# for k,v in piglinBartering.drop(9*9).items():
  
#     print(f'{k: <18}: {v}')