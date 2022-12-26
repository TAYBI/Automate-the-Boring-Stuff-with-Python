from pathlib import Path


# creating the folder when I will store the files
folder = Path(Path.cwd() / 'MadLibs')
# Path.mkdir(folder)


# Creating file with the origin text
fileOT = open(folder / 'fileOT.txt', 'w')
fileOT.write(
    'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
fileOT.close()

# creaying the file
fileOT = open(folder / 'fileOT.txt', 'r')
# gettin the orignal string
textO = fileOT.read()
# the words tha we need to replace
words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

for word in words:
    if word in textO:
        # printing 'an' enstad of 'a' if the words start with 'a'
        if (word.lower()[0] == 'a'):
            print('Enter an', word.lower())
        else:
            print('Enter a', word.lower())

        # replacing the words foudes by the new user input
        newWord = input()
        textO = textO.replace(word, newWord)

# saving the updates into the new file
fileNT = open(folder / 'fileNT.txt', 'w')
fileNT.write(textO)
fileNT.close()

# print(textO)
