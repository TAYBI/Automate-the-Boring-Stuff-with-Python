from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

browser = webdriver.Firefox()
browser.get('https://play2048.co')
html = browser.find_element(By.TAG_NAME, 'html')
KeysList = [Keys.DOWN, Keys.LEFT, Keys.RIGHT, Keys.UP]

while True:
    html.send_keys(KeysList[random.randint(0, 3)])
    time.sleep(1)
    try:
        gameOverElement = browser.find_element(By.CLASS_NAME, 'game-over')
        score = browser.find_element(By.CLASS_NAME, 'score-container')
        print('Sorry it over')
        print('Your score is:' + score.text)
        break
    except:
        continue

exit()
