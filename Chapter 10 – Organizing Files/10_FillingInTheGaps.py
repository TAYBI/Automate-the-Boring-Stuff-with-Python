#
# finds all files with a given prefix
#             such as spam001.txt, spam002.txt, and so on, in a single folder and
# locates any gaps in the numbering
#             (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
# rename all the later files to close this gap.
#
#
# added challenge,
# > write another program that can:
# >    insert gaps into numbered files so that a new file can be added


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
