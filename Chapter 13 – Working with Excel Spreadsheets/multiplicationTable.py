import sys

number = int(sys.argv[1])

for i in range(1, number):
    for j in range(1, number):
        print(str(i*j) + "\t", end="")
    print()
