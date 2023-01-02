import sys
import webbrowser
import pyperclip


if (len(sys.argv) > 1):
    # Get address from command line.
    adress = ''.join(sys.argv[1:])

else:
    # 3 Get the adress from clipboard
    # 870 Valencia St, San Francisco, CA 9   4110
    # You should copy this before you ruhn  the program
    adress = pyperclip.paste()

<<<<<<< HEAD
webbrowser.open('https://www.google.com/maps/place/' + adress)
=======
webbrowser.open(f'https://www.google.com/maps/place/{adress}')
>>>>>>> 015ea71ff6ba1e3aabb22d90115bc21f0a0e0107
