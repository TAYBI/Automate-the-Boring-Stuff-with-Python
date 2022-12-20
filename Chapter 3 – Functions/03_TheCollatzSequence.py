

def Collatz(number):
    if(number == 1):
        print("Yey you reatch 1")
        exit()
    elif (number % 2 == 0):
        print(number // 2)
        Collatz(number // 2)
    else:
        print(number * 3 + 1)
        Collatz(number * 3 + 1)


numberCollatz = 2

while numberCollatz != 1:

    try:
        numbER = int(input('Enter a number :'))
    except ValueError:
        print('Error: non Input value program will exit')
        exit()

    numberCollatz = Collatz(numbER)
    print(numberCollatz)
