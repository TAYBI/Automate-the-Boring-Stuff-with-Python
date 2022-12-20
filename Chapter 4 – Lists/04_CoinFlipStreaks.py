import random


numberOfStreaks = 0

for experementNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.,
    headsOrTails = ['T', 'H']
    ListOfHeadsOrTails = []
    streak = 0

    for item in range(100):
        ListOfHeadsOrTails.append(random.choice(headsOrTails))

    # print(ListOfHeadsOrTails)
    # break
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(ListOfHeadsOrTails)):
        if ListOfHeadsOrTails[i] == ListOfHeadsOrTails[i - 1]:
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))
