import pyinputplus as pyip
import random
import time


numberQuestions = 3
correctAnswers = 0

for i in range(numberQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#question : %s => %s x %s = ' % (i, num1, num2)
    try:
        pyip.inputStr(prompt=prompt, allowRegexes=['^%s$' % (
            num1 * num2)], blockRegexes=['.*', 'Incorrect'], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries')
    else:
        print('Correct !')
        correctAnswers += 1

    time.sleep(1)

print('-' * 3 + 'Score: %s / %s' % (correctAnswers, numberQuestions))
