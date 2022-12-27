import shutil
import os
from pathlib import Path
import pyinputplus as pyip


extensions = ['pdf', 'jpg', 'txt']
extension = pyip.inputMenu(extensions)

folder = Path.cwd() / 'FileDates'
newFolder = Path.cwd() / 'Newfolder'

# Create the new folder whare we will put the files founded if not already exist
if os.path.exists(newFolder) is False:
    Path.mkdir(newFolder)

# foldername, subfilderrs, filenames
for foldernames, subfolders, filenames in os.walk(folder):

    print('Files found in the', os.path.basename(foldernames), 'Folder:')
    for file in filenames:

        # check if the file founded ended with the extension wanted
        if os.path.basename(file).endswith(extension):

            # finding the absolut path of the file founded
            absFileName = os.path.join(os.path.abspath(foldernames), file)
            # finding the absolut path of the new distination
            newabs = os.path.join(os.path.abspath(newFolder), file)

            print(f'Old: {absFileName}\nNew: {newabs}\n')

            # copy the files from there location to the new folder.
            shutil.copy(absFileName, newFolder)
    print('>>'*20)
    print()

print('Done')
