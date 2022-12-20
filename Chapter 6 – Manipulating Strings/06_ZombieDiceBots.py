import zombiedice


class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResult = zombiedice.roll()
        brains = 0

        while diceRollResult is not None:
            brains += diceRollResult['brains']
            if brains <= 2:
                brains = zombiedice.roll()
            else:
                break


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Util Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name='Stop at 1 shotguns', minShotguns=1),
    MyZombie(name='Zombie Boot 1'),
    MyZombie(name='Zombie Boot 2'),
    MyZombie(name='Zombie Boot 3'),
)

# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)


# TODO: A bot that, after the first roll, randomly decides if it will or stop
# TODO: A bot that stops rolling after it has rolled two brains
# TODO: A bot that stops rolling after it has rolled two shotguns
# TODO: A bot that initially decides it’ll roll the dice one to four times but will stop early if it rolls two shotguns
# TODO: A bot that stops rolling after it has rolled more shotguns than brains
