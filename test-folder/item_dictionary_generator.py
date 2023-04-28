import os

directory = './test-folder/items'
dirlist = os.listdir(directory)
itemlist = set([filename.split('.')[0].rstrip("_0123456789")+'\n' for filename in dirlist])
# print(sorted(list(itemlist)))

# itemsFile = open('./test-folder/items.txt','w')
# itemsFile.writelines(sorted(list(itemlist)))
# itemsFile.close()




speedrunItemsFile = open('./test-folder/speedrun_items.txt','r')
speedrunItemsList = speedrunItemsFile.readlines()
for i in range(len(speedrunItemsList)):
    speedrunItemsList[i] = speedrunItemsList[i][:-1]
speedrunItemsFile.close()

print(speedrunItemsList)

# print(itemlist)