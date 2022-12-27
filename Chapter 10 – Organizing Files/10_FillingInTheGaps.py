from pathlib import Path
import shutil
import os
import random

# delliting old folders I created for the previous chaleges and programs
# folder1 = Path.cwd() / 'FileDates'
# folder2 = Path.cwd() / 'Newfolder'

# shutil.rmtree(folder1)
# shutil.rmtree(folder2)

# Create a folder containes the prefix
folder = Path.cwd() / 'NewFolder'
if not os.path.isdir(folder):
    Path.mkdir(folder)

# Create the envirement needed for starting the chalenge
# listOfrandomGaps = [random.randint(1, 100), random.randint(
#     1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

# print(listOfrandomGaps)

# for i in range(100):
#     if i not in listOfrandomGaps:
#         file = open(folder / f'spam{(i+1):03d}.txt', 'w')
# file.close()

prefix = 'spam'
list_ = []
listINt = []
# extention = ''

for folders, subfoldes, files in os.walk(folder):
    for filename in files:
        if filename.startswith(prefix):
            base_name, extension = os.path.splitext(filename)

            valueOfOrders = int(base_name.replace(prefix, ''))
            listINt.append(valueOfOrders)
            # print(int(base_name.replace(prefix, '')))
            list_.append(filename)

# founding the gaps
for i in range(len(listINt) - 2):
    if listINt[i] + 1 != listINt[i+1]:
        # rename all the later files to close this gap.
        oldName = f'{prefix}{listINt[i+1]:03d}{extension}'
        newName = f'{prefix}{(listINt[i+1] - 1):03d}{extension}'
        print(oldName, '>', newName)
        shutil.move(folder / f'{oldName}', folder / f'{newName}')

print(len(listINt), listINt)
print(list_)
