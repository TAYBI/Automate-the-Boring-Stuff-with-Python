import random

guess = ''
toss = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss ! Enter heads or tails: ')
    guess = input()


# 1 for heads
# 0 for tails

rndm = random.randint(0, 1)

if rndm == 1:
    toss = 'heads'
else:
    toss = 'tails'

if toss == guess:
    print('You got it ! congrats')
else:
    print('Nope, Guess again ')
    guess = input()
    if toss == guess:
        print('You got it ! congrats')
    else:
        print('Nope. You are really bad at this game.')
        print('The cion was :', toss)
