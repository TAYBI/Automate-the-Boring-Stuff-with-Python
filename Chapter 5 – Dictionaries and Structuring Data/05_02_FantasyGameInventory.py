import random


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']
inv = {'gold coin': 42, 'rope': 1}


def addToInventory(inventory, addedItems):
  for item in addedItems:
    if item in inventory:
      inventory[item] += 1
    else:
      inventory[item] = 1

  return inventory 

def displayInventory(dict):
  print("Inventory:")
  sum = 0
  for item in dict:
    sum += int(dict[item])
    print(dict[item], item)

  print('totlat number of items', sum)


inv = addToInventory(inv, dragonLoot)
displayInventory(inv)