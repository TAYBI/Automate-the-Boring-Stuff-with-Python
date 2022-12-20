
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['apples', 'oranges', 'cherries', 'banana', 'moose', 'goose']]


def maxLenght(listData):
    tableDataLenght = []
    for data in listData:
        tableDataLenght.append(len(' '.join(data)))

    return max(tableDataLenght)


for data in tableData:
    dataLenght = len(' '.join(data))
    maxLenght_ = maxLenght(tableData)
    if dataLenght <= maxLenght_:
        print(' ' * (maxLenght_ - dataLenght), ' '.join(data))
