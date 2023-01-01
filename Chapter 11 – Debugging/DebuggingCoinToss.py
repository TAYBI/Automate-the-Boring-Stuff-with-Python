import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss ! Enter heads or tails: ')
    guess = input()


# 1 for heads
# 0 for tails

toss = random.randint(0, 1)
if toss == guess:
    print('You got it ! congrats')
else:
    print('Nope, Guess again ')
    guess = input()
    if toss == guess:
        print('You got it ! congrats')
    else:
        print('Nope. You are really bad at this game.')
