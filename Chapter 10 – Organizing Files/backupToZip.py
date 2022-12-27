import zipfile
import os


def backupZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)
    # Figure out the filename this code should use based on
    # what files already exist.

    number = 1
    while True:
        zipFilenAME = f'{os.path.basename(folder)}_{number}.zip'
        print(zipFilenAME)
        if not os.path.abspath(zipFilenAME):
            break

        # Create the ZIP file.

        print(f'creating {zipFilenAME}...')
        backupZip = zipfile.ZipFile(zipFilenAME, 'w')
        # # TODO: Walk the entire folder tree and compress the files in each folder.
        for foldername, subfilderrs, filenames in os.walk(folder):
            print('Adding files in ', foldername)
            # Add the current folder to the ZIP file.
            backupZip.write(foldername)

            # Add all the files in this folder to the ZIP file.
            for filename in filenames:
                newBase = os.path.basename(filename) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
                backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        break
    print('Done.')


backupZip("C:\\Users\\DELL\\Desktop\\Automate the Boring Stuff with Python\\Chapter 10 – Organizing Files\\FileDates")
