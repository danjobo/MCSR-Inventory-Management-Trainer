from loot_table_generator import *


buriedTreasure = RDSTable()


# Underwater Pool
buriedTreasure.addPool(RDSPool((1,1),'Underwater Pool'))
buriedTreasure.getPools()[0].addItem(RDSItem(
    'heart_of_the_sea',
    (1,1),
    (1,1)
    ))

# Useful Pool
buriedTreasure.addPool(RDSPool((5,8),'Useful Pool'))
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
buriedTreasure.addPool(RDSPool((1,4),'Rare Pool'))
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
buriedTreasure.addPool(RDSPool((0,1),'Equipment Pool'))
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
buriedTreasure.addPool(RDSPool((2,2),'Food Pool'))
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
buriedTreasure.addPool(RDSPool((0,2),'Potion Pool'))
buriedTreasure.getPools()[5].addItem(RDSItem(
    'potion_of_water_breathing',
    (1,1),
    (1,1)
    ))






piglinBartering = RDSTable()



# Main Pool
piglinBartering.addPool(RDSPool((1,1),'Main Pool'))
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





if __name__ == "__main__":
    # buriedTreasure = RDSTable()
    # buriedTreasure.addPool(RDSPool((1,1)))

    # RDSPool.addItem(buriedTreasure.getPools()[0],RDSItem(
    #     'heart_of_the_sea',
    #     (1,1),
    #     (1/1)
    #     ))

    # print(RDSItem.getrdsName(RDSPool.getItems(buriedTreasure.getPools()[0])[0]))

    # print(buriedTreasure.getPools()[0].getItems()[0].getrdsName())

    # i = 0
    # for pool in buriedTreasure.getPools():
    #     i += 1
    #     print(f'Pool {i}')
    #     for item in pool.getItems():
    #         print(item.getrdsName())


    print(buriedTreasure.getPools())

    for k,v in buriedTreasure.generate().items():
        print(f'{k: <18}: {v}')


    # Would be easier to access pools if you could acces them by name, like a dictionary


    # print(piglinBartering.drop(5))

    for k,v in piglinBartering.drop(9*9).items():
      
        print(f'{k: <18}: {v}')