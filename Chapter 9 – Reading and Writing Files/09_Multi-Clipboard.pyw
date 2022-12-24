import pyperclip
import sys
import shelve


mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3:
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(mcbShelf.keys()))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
