# def boxPoint(symbol, width, height):
#     if(len(symbol)) != 1:
#         raise Exception('Symbole mus be a single charater string.')
#     if width <= 2:
#         raise Exception('width must be greater than 2.')
#     if height <= 2:
#         raise Exception('height must be grater than 2.')

#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + ('' * (width-2)) + symbol)
#     print(symbol *  width)

# for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         boxPoint(sym, w, h)
#     except Exception as err:
#         print('An exception happend: ' + str(err))


# def spam():
#     bacon()


# def bacon():
#     raise Exception('This the error message')


# spam()


#  Getting the Traceback as a String
# import traceback

# try:
#     raise Exception('This is a merror msg')
# except:
#     errorFile = open('errorFile.txt', 'w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('the traceback info was written to errorFile.txt')


# Assertions

# ages = [25, 36, 589, 80, 1, 15, 18]
# ages.sort()
# ages.reverse()
# assert ages[0] <= ages[-1]

# Using an Assertion in a Traffic Light Simulation
# market_2nd = {'ns': 'green', 'ew': 'red'}
# mission_16th = {'ns': 'red', 'ew': 'green'}


# def switchLights(stoplight):
#     for key in stoplight.keys():
#         if stoplight[key] == 'green':
#             stoplight[key] = 'yellow'
#         elif stoplight[key] == 'yellow':
#             stoplight[key] = 'red'
#         elif stoplight[key] == 'red':
#             stoplight[key] = 'green'
#     assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)


# switchLights(market_2nd)


# Logging

# import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format=' %(asctime)s - %(levelname)s - %(message)s')

# logging.debug('Strat of program')


# def factorial(n):
#     logging.debug('Start of Factorial(%s%%)' % n)
#     total = 1
#     for i in range(1, n+1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial (%s%%)' % (n))

#     return total


# factorial(5)

# logging.debug('End of program')

# Logging Levels


# DEBUG


# logging.debug()


# The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.

# INFO


# logging.info()


# Used to record information on general events in your program or confirm that things are working at their point in the program.

# WARNING


# logging.warning()


# Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.

# ERROR


# logging.error()


# Used to record an error that caused the program to fail to do something.

# CRITICAL


# logging.critical()


# The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.
