import pyinputplus as pyip


def addsUpToTen(numbers):

    numbersList = list(numbers)

    for i in range(len(numbersList)):
        numbersList[i] = int(numbersList[i])

    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %
                        (sum(numbersList)))

    return int(numbers)


# pyip.inputNum(prompt="Enter a number that adds up to 10: ")
pyip.inputCustom(addsUpToTen, prompt="Enter a number that adds up to 10: ")
