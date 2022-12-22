import pyinputplus as pyip


while True:
    response = pyip.inputYesNo(
        prompt="Want to know how to keep an idiot busy for hours?\n> ")

    if response == 'no' or response == 'NO' or response == 'No' or response == 'n':
        print('okey, have a anice day')
        exit()
