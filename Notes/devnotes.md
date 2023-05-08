# DevNotes

1. Add ordering system for how items get added into inventory grid in [[../test_folder/inventory_object_creation.py]]

ITEM MOVEMENT RULES:
- Shift Clicking from Hotbar
  1. Checks for empty/same inventory slot
      1. Adds to upper left most empty/same slot
  2. Doesn't move
- Shift Clicking from Inventory
  1. Checks for empty/same hotbar slot
      1. Adds to left most empty/same slot
  2. Doesn't move
- Shift Clicking from Craft Product Slot
  1. Checks for empty/same hotbar slot
      1. Adds to right most empty/same slot
  2. Checks for empty/same inventory slot
      1. Adds to lower right most empty/same slot
  3. Doesn't move
- Picking up Items
  1. Checks for empty/same hotbar slot
      1. Adds to left most empty/same slot
  2. Checks for empty/same inventory slot
      1. Adds to upper left most empty/same slot
  3. Doesn't pick up
- Shift Clicking from Equipment/Offhand Slot
  1. Checks for empty/same inventory slot
      1. Adds to upper left most empty/same item slot
  2. Checks for empty/same hotbar slot
      1. Adds to let most empty/same slot
  3. Doesn't move

2. Make Sprites click and draggable