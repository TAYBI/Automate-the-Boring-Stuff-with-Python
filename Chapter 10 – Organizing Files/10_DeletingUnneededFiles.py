import os

# Get the path of desktop directoryy
homeDir = os.path.expanduser('~')
deskPath = os.path.join(homeDir, 'Desktop')

print(deskPath)

sum_ = 0
for foldernames, subfolders, filenames in os.walk(deskPath):
    sizeInMB = os.path.getsize(foldernames) / 1024
    # it should be this one down below, but I mad it smaller so I can see the execution on my machine, (I dont have large files)
    # sizeInMB = os.path.getsize(foldernames) / 1024 / 1024
    # sum_ += sizeInMB
    for file in filenames:
        if sizeInMB >= 100:
            print(
                f'{os.path.basename(file)} >> located at {os.path.abspath(file)} --> {sizeInMB:.2f} MB')


# print('sum = ', sum_, sum_ / 1024, 'MB')
