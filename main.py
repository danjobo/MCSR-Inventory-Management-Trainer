'''
Program where the user can click and drag items that snap into a grid when dropped
'''

# FEATURES TO IMPLEMENT:
    # [X] Grid Coordinate Setting
        # [] Scalable based on resolution?
    # [X] Nearest Square Detection
        # [X] Hovers white square over selected slot
        # [] Snaps dropped items to nearest square
    # 


import csv
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Grid Snap Draggables')
root.iconbitmap('./images/end_crystal_icon_Tde_icon.ico')
root.geometry('1920x1080+0+0')

w = 1920
h = 800
x = w/2
y = h/2

mousex = 0
mousey = 0

invrow = 0
invitem = 0
hotrow = 0
hotitem = 0
armrow = 0
armitem = 0
offrow = 0
offitem = 0


breadx = 400
bready = 250
breadclicked = False


csv_list_storage = []
op = open('inventory.csv','r')
dt = csv.reader(op)
for row in dt:
    print(row)
    csv_list_storage.append(row)
for rowindex in range(len(csv_list_storage)):
    for itemindex in range(len(csv_list_storage[rowindex])):
        if csv_list_storage[rowindex][itemindex] == '_':
            csv_list_storage[rowindex][itemindex] = None
        else:
            csv_list_storage[rowindex][itemindex] = (
                csv_list_storage[rowindex][itemindex].split(':')[0],
                int(csv_list_storage[rowindex][itemindex].split(':')[1]) if csv_list_storage[rowindex][itemindex].split(':')[1] != ' ' else None
            )
print('\n\n\n')
print(csv_list_storage)
op.close()



holding = ['',None]
holdingBool = False





my_canvas = Canvas(root,width=w,height=h,bg='white')
my_canvas.pack()


breadimg = Image.open('./images/bread.png')
breadimg = breadimg.resize((47,47))
img = ImageTk.PhotoImage(breadimg)


breadcopy = Image.open('./images/bread copy.png')
breadcopy = breadcopy.resize((47,47))
breadcopyobj = ImageTk.PhotoImage(breadcopy)
apple = PhotoImage(file='./images/apple.png')
cat = PhotoImage(file='./cat.png')


inventory = Image.open('./images/inventory-snip.png')
inventory = inventory.resize((528,498))
inventoryobj = ImageTk.PhotoImage(inventory)

inventoryinst = my_canvas.create_image(960,450, image=inventoryobj)
my_image = my_canvas.create_image(400,250, anchor='nw', image=img)

inventory_storage = []
op = open('inventory.csv','r')
dt = csv.reader(op)
for row in dt:
    inventory_storage.append(row)
op.close()




# Alpha Support
transparent_images = []  # to hold the newly created image
def create_rectangle(x1, y1, x2, y2, **kwargs):
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        transparent_images.append(ImageTk.PhotoImage(image))
        return my_canvas.create_image(x1, y1, image=transparent_images[-1], anchor='nw')
    return my_canvas.create_rectangle(x1, y1, x2, y2, **kwargs)



# Generates the coordinates for inventory grid
topLeftX = 717
topLeftY = 450
xLength = 53
yLength = 53

inventory_coords = [[(topLeftX+(xLength*ix)+ix,topLeftY+(yLength*iy)+iy) for ix in range(10)] for iy in range(4)]

hotbar_coords = [[(topLeftX+(xLength*ix)+ix,(3*yLength+15)+topLeftY+(yLength*iy)+iy) for ix in range(10)] for iy in range(2)]

# Generates the coordinates for the equipment slots
topLeftY2 = 223

armor_coords = [[(topLeftX+(xLength*ix)+ix,topLeftY2+(yLength*iy)+iy) for ix in range(2)] for iy in range(5)]

topLeftX2 = 925
topLeftY3 = 384

offhand_coords = [[(topLeftX2+(xLength*ix)+ix,topLeftY3+(yLength*iy)+iy) for ix in range(2)] for iy in range(2)]







# Creates all event functions
def move(event):
    #event.x
    #event.y
    global breadx
    global bready
    global img
    global my_image
    global mousex
    global mousey
    global invrow
    global invitem
    global hotrow
    global hotitem
    global armrow
    global armitem
    global offrow
    global offitem
    global holdingBool
    global holding
    global heldImage
    # Detects mouse position
    if 696<=mousex<=1223:
        if 201<=mousey<=698:
            # Detects if mouse in inventory section
            if topLeftX<=mousex<=topLeftX+(xLength*9+8):
                # Detects if mouse in inventory storage
                if topLeftY<=mousey<=topLeftY+(yLength*3+2):
                    # Detects if mouse on inventory storage slot
                    if inventory_coords[0][0][0]<=mousex<=inventory_coords[1][1][0]:
                        if inventory_coords[0][0][1]<=mousey<=inventory_coords[1][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(\
                                inventory_coords[invrow][invitem][0],inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0
                            )
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (0,0)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(
                                inventory_coords[invrow][invitem][0],
                                inventory_coords[invrow][invitem][1],
                                inventory_coords[invrow+1][invitem+1][0],
                                inventory_coords[invrow+1][invitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.5
                            )
                        elif inventory_coords[1][0][1]<=mousey<=inventory_coords[2][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (1,0)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[2][0][1]<=mousey<=inventory_coords[3][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (2,0)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                    elif inventory_coords[0][1][0]<=mousex<=inventory_coords[1][2][0]:
                        if inventory_coords[0][0][1]<=mousey<=inventory_coords[1][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (0,1)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[1][0][1]<=mousey<=inventory_coords[2][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (1,1)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[2][0][1]<=mousey<=inventory_coords[3][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (2,1)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                    elif inventory_coords[0][2][0]<=mousex<=inventory_coords[1][3][0]:
                        if inventory_coords[0][0][1]<=mousey<=inventory_coords[1][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (0,2)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[1][0][1]<=mousey<=inventory_coords[2][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (1,2)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[2][0][1]<=mousey<=inventory_coords[3][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (2,2)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                    elif inventory_coords[0][3][0]<=mousex<=inventory_coords[1][4][0]:
                        if inventory_coords[0][0][1]<=mousey<=inventory_coords[1][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (0,3)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[1][0][1]<=mousey<=inventory_coords[2][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (1,3)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[2][0][1]<=mousey<=inventory_coords[3][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (2,3)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                    elif inventory_coords[0][4][0]<=mousex<=inventory_coords[1][5][0]:
                        if inventory_coords[0][0][1]<=mousey<=inventory_coords[1][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (0,4)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[1][0][1]<=mousey<=inventory_coords[2][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (1,4)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[2][0][1]<=mousey<=inventory_coords[3][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (2,4)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                    elif inventory_coords[0][5][0]<=mousex<=inventory_coords[1][6][0]:
                        if inventory_coords[0][0][1]<=mousey<=inventory_coords[1][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (0,5)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[1][0][1]<=mousey<=inventory_coords[2][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (1,5)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[2][0][1]<=mousey<=inventory_coords[3][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (2,5)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                    elif inventory_coords[0][6][0]<=mousex<=inventory_coords[1][7][0]:
                        if inventory_coords[0][0][1]<=mousey<=inventory_coords[1][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (0,6)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[1][0][1]<=mousey<=inventory_coords[2][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (1,6)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[2][0][1]<=mousey<=inventory_coords[3][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (2,6)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                    elif inventory_coords[0][7][0]<=mousex<=inventory_coords[1][8][0]:
                        if inventory_coords[0][0][1]<=mousey<=inventory_coords[1][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (0,7)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[1][0][1]<=mousey<=inventory_coords[2][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (1,7)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[2][0][1]<=mousey<=inventory_coords[3][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (2,7)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                    elif inventory_coords[0][8][0]<=mousex<=inventory_coords[1][9][0]:
                        if inventory_coords[0][0][1]<=mousey<=inventory_coords[1][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (0,8)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[1][0][1]<=mousey<=inventory_coords[2][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (1,8)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                        elif inventory_coords[2][0][1]<=mousey<=inventory_coords[3][1][1]:
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.0)
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            invrow, invitem = (2,8)
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(inventory_coords[invrow][invitem][0],\
                                                                                inventory_coords[invrow][invitem][1],inventory_coords[invrow+1][invitem+1][0],inventory_coords[invrow+1][invitem+1][1],fill='#ffffff',width=0,alpha=.5)
                # Detects if mouse in hotbar
                elif (3*yLength+15)+topLeftY<=mousey<=(3*yLength+15)+topLeftY+(yLength):
                    # Detects if mouse on hotbar slot
                    if hotbar_coords[0][0][0]<=mousex<=hotbar_coords[1][1][0]:
                        if hotbar_coords[0][0][1]<=mousey<=hotbar_coords[1][1][1]:
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(
                                inventory_coords[invrow][invitem][0],
                                inventory_coords[invrow][invitem][1],
                                inventory_coords[invrow+1][invitem+1][0],
                                inventory_coords[invrow+1][invitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotitem] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            hotrow, hotitem = (0,0)
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotitem] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.5
                            )
                    elif hotbar_coords[0][1][0]<=mousex<=hotbar_coords[1][2][0]:
                        if hotbar_coords[0][0][1]<=mousey<=hotbar_coords[1][1][1]:
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(
                                inventory_coords[invrow][invitem][0],
                                inventory_coords[invrow][invitem][1],
                                inventory_coords[invrow+1][invitem+1][0],
                                inventory_coords[invrow+1][invitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            hotrow, hotitem = (0,1)
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotitem] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.5
                            )
                    elif hotbar_coords[0][2][0]<=mousex<=hotbar_coords[1][3][0]:
                        if hotbar_coords[0][0][1]<=mousey<=hotbar_coords[1][1][1]:
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(
                                inventory_coords[invrow][invitem][0],
                                inventory_coords[invrow][invitem][1],
                                inventory_coords[invrow+1][invitem+1][0],
                                inventory_coords[invrow+1][invitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            hotrow, hotitem = (0,2)
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotitem] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.5
                            )
                    elif hotbar_coords[0][3][0]<=mousex<=hotbar_coords[1][4][0]:
                        if hotbar_coords[0][0][1]<=mousey<=hotbar_coords[1][1][1]:
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(
                                inventory_coords[invrow][invitem][0],
                                inventory_coords[invrow][invitem][1],
                                inventory_coords[invrow+1][invitem+1][0],
                                inventory_coords[invrow+1][invitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            hotrow, hotitem = (0,3)
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotitem] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.5
                            )
                    elif hotbar_coords[0][4][0]<=mousex<=hotbar_coords[1][5][0]:
                        if hotbar_coords[0][0][1]<=mousey<=hotbar_coords[1][1][1]:
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(
                                inventory_coords[invrow][invitem][0],
                                inventory_coords[invrow][invitem][1],
                                inventory_coords[invrow+1][invitem+1][0],
                                inventory_coords[invrow+1][invitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            hotrow, hotitem = (0,4)
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotitem] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.5
                            )
                    elif hotbar_coords[0][5][0]<=mousex<=hotbar_coords[1][6][0]:
                        if hotbar_coords[0][0][1]<=mousey<=hotbar_coords[1][1][1]:
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(
                                inventory_coords[invrow][invitem][0],
                                inventory_coords[invrow][invitem][1],
                                inventory_coords[invrow+1][invitem+1][0],
                                inventory_coords[invrow+1][invitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            hotrow, hotitem = (0,5)
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotitem] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.5
                            )
                    elif hotbar_coords[0][6][0]<=mousex<=hotbar_coords[1][7][0]:
                        if hotbar_coords[0][0][1]<=mousey<=hotbar_coords[1][1][1]:
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(
                                inventory_coords[invrow][invitem][0],
                                inventory_coords[invrow][invitem][1],
                                inventory_coords[invrow+1][invitem+1][0],
                                inventory_coords[invrow+1][invitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            hotrow, hotitem = (0,6)
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotitem] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.5
                            )
                    elif hotbar_coords[0][7][0]<=mousex<=hotbar_coords[1][8][0]:
                        if hotbar_coords[0][0][1]<=mousey<=hotbar_coords[1][1][1]:
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(
                                inventory_coords[invrow][invitem][0],
                                inventory_coords[invrow][invitem][1],
                                inventory_coords[invrow+1][invitem+1][0],
                                inventory_coords[invrow+1][invitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            hotrow, hotitem = (0,7)
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotitem] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.5
                            )
                    elif hotbar_coords[0][8][0]<=mousex<=hotbar_coords[1][9][0]:
                        if hotbar_coords[0][0][1]<=mousey<=hotbar_coords[1][1][1]:
                            my_canvas.delete(inventory_rects[invrow][invitem])
                            inventory_rects[invrow][invitem] = create_rectangle(
                                inventory_coords[invrow][invitem][0],
                                inventory_coords[invrow][invitem][1],
                                inventory_coords[invrow+1][invitem+1][0],
                                inventory_coords[invrow+1][invitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotrow] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(armor_rects[armrow][armitem])
                            armor_rects[armrow][armitem] = create_rectangle(
                                armor_coords[armrow][armitem][0],
                                armor_coords[armrow][armitem][1],
                                armor_coords[armrow+1][armitem+1][0],
                                armor_coords[armrow+1][armitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            my_canvas.delete(offhand_rect[offrow][offitem])
                            offhand_rect[offrow][offitem] = create_rectangle(
                                hotbar_coords[offrow][offitem][0],
                                hotbar_coords[offrow][offitem][1],
                                hotbar_coords[offrow+1][offitem+1][0],
                                hotbar_coords[offrow+1][offitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.0
                            )
                            hotrow, hotitem = (0,8)
                            my_canvas.delete(hotbar_rects[hotrow][hotitem])
                            hotbar_rects[hotrow][hotitem] = create_rectangle(
                                hotbar_coords[hotrow][hotitem][0],
                                hotbar_coords[hotrow][hotitem][1],
                                hotbar_coords[hotrow+1][hotitem+1][0],
                                hotbar_coords[hotrow+1][hotitem+1][1],
                                fill='#ffffff',
                                width=0,
                                alpha=.5
                            )
                # Detects if mouse in offhand slot
                elif offhand_coords[0][0][1]<=mousey<=offhand_coords[1][1][1] and offhand_coords[0][0][0]<=mousex<=offhand_coords[1][1][0]:
                    my_canvas.delete(inventory_rects[invrow][invitem])
                    inventory_rects[invrow][invitem] = create_rectangle(
                        inventory_coords[invrow][invitem][0],
                        inventory_coords[invrow][invitem][1],
                        inventory_coords[invrow+1][invitem+1][0],
                        inventory_coords[invrow+1][invitem+1][1],
                        fill='#ffffff',
                        width=0,
                        alpha=.0
                    )
                    my_canvas.delete(hotbar_rects[hotrow][hotitem])
                    hotbar_rects[hotrow][hotitem] = create_rectangle(
                        hotbar_coords[hotrow][hotitem][0],
                        hotbar_coords[hotrow][hotitem][1],
                        hotbar_coords[hotrow+1][hotitem+1][0],
                        hotbar_coords[hotrow+1][hotitem+1][1],
                        fill='#ffffff',
                        width=0,
                        alpha=.0
                    )
                    my_canvas.delete(armor_rects[armrow][armitem])
                    armor_rects[armrow][armitem] = create_rectangle(
                        armor_coords[armrow][armitem][0],
                        armor_coords[armrow][armitem][1],
                        armor_coords[armrow+1][armitem+1][0],
                        armor_coords[armrow+1][armitem+1][1],
                        fill='#ffffff',
                        width=0,
                        alpha=.0
                    )
                    my_canvas.delete(offhand_rect[offrow][offitem])
                    offhand_rect[offrow][offitem] = create_rectangle(
                        hotbar_coords[offrow][offitem][0],
                        hotbar_coords[offrow][offitem][1],
                        hotbar_coords[offrow+1][offitem+1][0],
                        hotbar_coords[offrow+1][offitem+1][1],
                        fill='#ffffff',
                        width=0,
                        alpha=.0
                    )
                    offrow, offitem = (0,0)
                    my_canvas.delete(offhand_rect[offrow][offitem])
                    offhand_rect[offrow][offitem] = create_rectangle(
                            offhand_coords[offrow][offitem][0],
                            offhand_coords[offrow][offitem][1],
                            offhand_coords[offrow+1][offitem+1][0],
                            offhand_coords[offrow+1][offitem+1][1],
                            fill='#ffffff',
                            width=0,
                            alpha=.5
                        )
                # Detects if mouse in equipment
                elif topLeftY2<=mousey<=topLeftY2+(yLength*4)+4:
                  # Detects if mouse in armor slots
                  if armor_coords[0][0][0]<=mousex<=armor_coords[1][1][0]:
                      if armor_coords[0][0][1]<=mousey<=armor_coords[1][1][1]:
                          my_canvas.delete(inventory_rects[invrow][invitem])
                          inventory_rects[invrow][invitem] = create_rectangle(
                              inventory_coords[invrow][invitem][0],
                              inventory_coords[invrow][invitem][1],
                              inventory_coords[invrow+1][invitem+1][0],
                              inventory_coords[invrow+1][invitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(hotbar_rects[hotrow][hotitem])
                          hotbar_rects[hotrow][hotitem] = create_rectangle(
                              hotbar_coords[hotrow][hotitem][0],
                              hotbar_coords[hotrow][hotitem][1],
                              hotbar_coords[hotrow+1][hotitem+1][0],
                              hotbar_coords[hotrow+1][hotitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(armor_rects[armrow][armitem])
                          armor_rects[armrow][armitem] = create_rectangle(
                              armor_coords[armrow][armitem][0],
                              armor_coords[armrow][armitem][1],
                              armor_coords[armrow+1][armitem+1][0],
                              armor_coords[armrow+1][armitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(offhand_rect[offrow][offitem])
                          offhand_rect[offrow][offitem] = create_rectangle(
                              hotbar_coords[offrow][offitem][0],
                              hotbar_coords[offrow][offitem][1],
                              hotbar_coords[offrow+1][offitem+1][0],
                              hotbar_coords[offrow+1][offitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          armrow, armitem = (0,0)
                          my_canvas.delete(armor_rects[armrow][armitem])
                          armor_rects[armrow][armitem] = create_rectangle(
                              armor_coords[armrow][armitem][0],
                              armor_coords[armrow][armitem][1],
                              armor_coords[armrow+1][armitem+1][0],
                              armor_coords[armrow+1][armitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.5
                          )
                      elif armor_coords[1][0][1]<=mousey<=armor_coords[2][1][1]:
                          my_canvas.delete(inventory_rects[invrow][invitem])
                          inventory_rects[invrow][invitem] = create_rectangle(
                              inventory_coords[invrow][invitem][0],
                              inventory_coords[invrow][invitem][1],
                              inventory_coords[invrow+1][invitem+1][0],
                              inventory_coords[invrow+1][invitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(hotbar_rects[hotrow][hotitem])
                          hotbar_rects[hotrow][hotitem] = create_rectangle(
                              hotbar_coords[hotrow][hotitem][0],
                              hotbar_coords[hotrow][hotitem][1],
                              hotbar_coords[hotrow+1][hotitem+1][0],
                              hotbar_coords[hotrow+1][hotitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(armor_rects[armrow][armitem])
                          armor_rects[armrow][armitem] = create_rectangle(
                              armor_coords[armrow][armitem][0],
                              armor_coords[armrow][armitem][1],
                              armor_coords[armrow+1][armitem+1][0],
                              armor_coords[armrow+1][armitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(offhand_rect[offrow][offitem])
                          offhand_rect[offrow][offitem] = create_rectangle(
                              hotbar_coords[offrow][offitem][0],
                              hotbar_coords[offrow][offitem][1],
                              hotbar_coords[offrow+1][offitem+1][0],
                              hotbar_coords[offrow+1][offitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          armrow, armitem = (1,0)
                          my_canvas.delete(armor_rects[armrow][armitem])
                          armor_rects[armrow][armitem] = create_rectangle(
                              armor_coords[armrow][armitem][0],
                              armor_coords[armrow][armitem][1],
                              armor_coords[armrow+1][armitem+1][0],
                              armor_coords[armrow+1][armitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.5
                          )
                      elif armor_coords[2][0][1]<=mousey<=armor_coords[3][1][1]:
                          my_canvas.delete(inventory_rects[invrow][invitem])
                          inventory_rects[invrow][invitem] = create_rectangle(
                              inventory_coords[invrow][invitem][0],
                              inventory_coords[invrow][invitem][1],
                              inventory_coords[invrow+1][invitem+1][0],
                              inventory_coords[invrow+1][invitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(hotbar_rects[hotrow][hotitem])
                          hotbar_rects[hotrow][hotitem] = create_rectangle(
                              hotbar_coords[hotrow][hotitem][0],
                              hotbar_coords[hotrow][hotitem][1],
                              hotbar_coords[hotrow+1][hotitem+1][0],
                              hotbar_coords[hotrow+1][hotitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(armor_rects[armrow][armitem])
                          armor_rects[armrow][armitem] = create_rectangle(
                              armor_coords[armrow][armitem][0],
                              armor_coords[armrow][armitem][1],
                              armor_coords[armrow+1][armitem+1][0],
                              armor_coords[armrow+1][armitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(offhand_rect[offrow][offitem])
                          offhand_rect[offrow][offitem] = create_rectangle(
                              hotbar_coords[offrow][offitem][0],
                              hotbar_coords[offrow][offitem][1],
                              hotbar_coords[offrow+1][offitem+1][0],
                              hotbar_coords[offrow+1][offitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          armrow, armitem = (2,0)
                          my_canvas.delete(armor_rects[armrow][armitem])
                          armor_rects[armrow][armitem] = create_rectangle(
                              armor_coords[armrow][armitem][0],
                              armor_coords[armrow][armitem][1],
                              armor_coords[armrow+1][armitem+1][0],
                              armor_coords[armrow+1][armitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.5
                          )
                      elif armor_coords[3][0][1]<=mousey<=armor_coords[4][1][1]:
                          my_canvas.delete(inventory_rects[invrow][invitem])
                          inventory_rects[invrow][invitem] = create_rectangle(
                              inventory_coords[invrow][invitem][0],
                              inventory_coords[invrow][invitem][1],
                              inventory_coords[invrow+1][invitem+1][0],
                              inventory_coords[invrow+1][invitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(hotbar_rects[hotrow][hotitem])
                          hotbar_rects[hotrow][hotitem] = create_rectangle(
                              hotbar_coords[hotrow][hotitem][0],
                              hotbar_coords[hotrow][hotitem][1],
                              hotbar_coords[hotrow+1][hotitem+1][0],
                              hotbar_coords[hotrow+1][hotitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(armor_rects[armrow][armitem])
                          armor_rects[armrow][armitem] = create_rectangle(
                              armor_coords[armrow][armitem][0],
                              armor_coords[armrow][armitem][1],
                              armor_coords[armrow+1][armitem+1][0],
                              armor_coords[armrow+1][armitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          my_canvas.delete(offhand_rect[offrow][offitem])
                          offhand_rect[offrow][offitem] = create_rectangle(
                              hotbar_coords[offrow][offitem][0],
                              hotbar_coords[offrow][offitem][1],
                              hotbar_coords[offrow+1][offitem+1][0],
                              hotbar_coords[offrow+1][offitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.0
                          )
                          armrow, armitem = (3,0)
                          my_canvas.delete(armor_rects[armrow][armitem])
                          armor_rects[armrow][armitem] = create_rectangle(
                              armor_coords[armrow][armitem][0],
                              armor_coords[armrow][armitem][1],
                              armor_coords[armrow+1][armitem+1][0],
                              armor_coords[armrow+1][armitem+1][1],
                              fill='#ffffff',
                              width=0,
                              alpha=.5
                          )
                  else:
                      my_canvas.delete(hotbar_rects[hotrow][hotitem])
                      my_canvas.delete(inventory_rects[invrow][invitem])
                      my_canvas.delete(armor_rects[armrow][armitem])
                      my_canvas.delete(offhand_rect[offrow][offitem])
                else:
                    my_canvas.delete(hotbar_rects[hotrow][hotitem])
                    my_canvas.delete(inventory_rects[invrow][invitem])
                    my_canvas.delete(armor_rects[armrow][armitem])
                    my_canvas.delete(offhand_rect[offrow][offitem])
            else:
                my_canvas.delete(hotbar_rects[hotrow][hotitem])
                my_canvas.delete(inventory_rects[invrow][invitem])
                my_canvas.delete(armor_rects[armrow][armitem])
                my_canvas.delete(offhand_rect[offrow][offitem])
        else:
            my_canvas.delete(hotbar_rects[hotrow][hotitem])
            my_canvas.delete(inventory_rects[invrow][invitem])
            my_canvas.delete(armor_rects[armrow][armitem])
            my_canvas.delete(offhand_rect[offrow][offitem])
    else:
        my_canvas.delete(hotbar_rects[hotrow][hotitem])
        my_canvas.delete(inventory_rects[invrow][invitem])
        my_canvas.delete(armor_rects[armrow][armitem])
        my_canvas.delete(offhand_rect[offrow][offitem])
    if breadclicked == True:
      img = ImageTk.PhotoImage(breadimg)
      my_image = my_canvas.create_image(event.x,event.y, image=img)
      my_canvas.tag_raise(my_image)
      breadx = event.x
      bready = event.y
    mousex = event.x
    mousey = event.y
    coord_label.config(text="Coordinates x: " + str(event.x) + ' y: ' + str(event.y) + "\t Bread x: " + str(breadx) + ' y: ' + str(bready))



    # Detects if holdling an item
    if holdingBool:
        heldImage = my_canvas.create_image(event.x, event.y, image=img)



    # print(inventoryinst)
    # Detects if mouse is inside inventory window
    # print()
    # print(my_image)
    # print()
    # print(inventory_rects)
    # print()
    # print(hotbar_rects)

def click(event):
    #event.x
    #event.y
    global breadclicked
    global breadx
    global bready
    global my_image
    global img
    if breadclicked == False and breadx - 25 <= event.x <= breadx + 25 and\
    bready - 25 <= event.y <= bready + 25:
        my_canvas.delete(my_image)
        my_image = my_canvas.create_image(event.x,event.y, image=img)
        my_canvas.tag_raise(my_image)
        breadx = event.x
        bready = event.y
        breadclicked = True
    elif breadclicked == True and breadx - 25 <= event.x <= breadx + 25 and\
    bready - 25 <= event.y <= bready + 25:
        breadclicked = False
    click_label['text'] = 'Clicked: ' + str(breadclicked)

def rclick(event):
    #event.x
    #event.y
    global breadclicked
    global img
    global breadcopyobj
    global breadcopyinst
    global mousex
    global mousey
    if breadclicked == True:
        breadcopyinst = my_canvas.create_image(mousex,mousey, image=breadcopyobj)

def a_press(event):
    global mousex
    global mousey
    global apple
    global appleimg
    appleimg = my_canvas.create_image(mousex,mousey, image=apple)

def c_press(event):
    global mousex
    global mousey
    global apple
    global catimg
    catimg = my_canvas.create_image(mousex,mousey, image=cat)

def x_press(event):
    global inventory
    global inventoryobj
    global inventoryinst
    global my_image
    global img
    global breadclicked
    global breadx
    global bready
    my_canvas.delete('all')
    inventoryinst = my_canvas.create_image(960,450, image=inventoryobj)
    my_image = my_canvas.create_image(400,250, anchor='nw', image=img)
    breadclicked = False
    breadx = 400
    bready = 250





# Displays object info
coord_label = Label(root,text='')
coord_label.pack(pady=10)

click_label = Label(root,text='')
click_label.pack(pady=3)

bread_grid_label = Label(root,text='')
bread_grid_label.pack(pady=1)




# Stores all hotbar overlay rectangles in lists
inventory_rects = []
for rownum in range(len(inventory_coords)-1):
    inventory_rects.append([])
    for itemnum in range(len(inventory_coords[rownum])-1):
        inventory_rects[rownum].append(create_rectangle(
            inventory_coords[rownum][itemnum][0],
            inventory_coords[rownum][itemnum][1],
            inventory_coords[rownum+1][itemnum+1][0],
            inventory_coords[rownum+1][itemnum+1][1],
            fill='#ffffff',
            width=0,
            alpha=.0
        ))

hotbar_rects = []
for rownum in range(len(hotbar_coords)-1):
    hotbar_rects.append([])
    for itemnum in range(len(hotbar_coords[rownum])-1):
        hotbar_rects[rownum].append(create_rectangle(
            hotbar_coords[rownum][itemnum][0],
            hotbar_coords[rownum][itemnum][1],
            hotbar_coords[rownum+1][itemnum+1][0],
            hotbar_coords[rownum+1][itemnum+1][1],
            fill='#ffffff',
            width=0,
            alpha=.0
        ))

armor_rects = []
for rownum in range(len(armor_coords)-1):
    armor_rects.append([])
    for itemnum in range(len(armor_coords[rownum])-1):
        armor_rects[rownum].append(create_rectangle(
            armor_coords[rownum][itemnum][0],
            armor_coords[rownum][itemnum][1],
            armor_coords[rownum+1][itemnum+1][0],
            armor_coords[rownum+1][itemnum+1][1],
            fill='#ffffff',
            width=0,
            alpha=.0
        ))

offhand_rect = []
for rownum in range(len(offhand_coords)-1):
    offhand_rect.append([])
    for itemnum in range(len(offhand_coords[rownum])-1):
        offhand_rect[rownum].append(create_rectangle(
            offhand_coords[rownum][itemnum][0],
            offhand_coords[rownum][itemnum][1],
            offhand_coords[rownum+1][itemnum+1][0],
            offhand_coords[rownum+1][itemnum+1][1],
            fill='#ffffff',
            width=0,
            alpha=.0
        ))

# print(inventoryinst)
# print()
# print(my_image)
# print()
# print(inventory_rects)
# print()
# print(hotbar_rects)




# Creates new rectangles and deletes old ones
# my_canvas.delete(inventory_rects[0][0])
# inventory_rects[0][0] = create_rectangle(inventory_coords[0][0][0],inventory_coords[0][0][1],inventory_coords[1][1][0],inventory_coords[1][1][1],fill='#ffffff',width=0,alpha=.5)
# my_canvas.delete(inventory_rects[0][2])

# my_canvas.delete(hotbar_rects[0][0])
# hotbar_rects[0][0] = create_rectangle(hotbar_coords[0][0][0],hotbar_coords[0][0][1],hotbar_coords[1][1][0],hotbar_coords[1][1][1],fill='#ffffff',width=0,alpha=.5)
# my_canvas.delete(hotbar_rects[0][0])


                



# Binds keys to event functions
root.bind('<Button-1>', click)
root.bind('<Button-3>', rclick)
root.bind('<Motion>', move) #Regular moving the mouse around
root.bind('a', a_press)
root.bind('c', c_press)
root.bind('x', x_press)
# root.bind('<B1-Motion>', move) #Clicking and Dragging



# Initializes the main loop
root.mainloop()