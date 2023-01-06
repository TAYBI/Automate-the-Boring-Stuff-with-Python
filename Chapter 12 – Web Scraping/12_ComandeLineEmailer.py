from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Firefox()
url = 'https://accounts.google.com/AccountChooser/signinchooser'


def logIn(mail, password):
    browser.get('https://accounts.google.com/AccountChooser/signinchooser')
    emailElement = browser.find_element(By.ID, 'identifierId')
    emailElement.send_keys(mail)
    emailElement.send_keys(Keys.ENTER)
    myElem = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    passwordElement = browser.find_element(By.NAME, 'Passwd')
    passwordElement.send_keys(password)


# TODO: takes an email adress and string from the commande line

print('-'*10 + 'Login to your account' + '-'*10)

mail = input('Enter your email: ')
password = input('Enter your password: ')
browser.get(url)

emailElement = browser.find_element(By.ID, 'identifierId')
emailElement.send_keys(mail)
emailElement.send_keys(Keys.ENTER)

passwordElement = browser.find_element(By.NAME, 'Passwd')
element_present = EC.presence_of_element_located(passwordElement)
WebDriverWait(browser, 5).until(element_present)

passwordElement.send_keys(password)
passwordElement.send_keys(Keys.ENTER)
# emailElement = browser.find_element(By.ID, 'identifierId')

# emailElement.send_keys(mail)
# emailElement.send_keys(Keys.ENTER)
# logIn(mail, password)


# TODO: check if the imas vailde

text = input('Enter your txtt you want to send: ')

# TODO: log to google account


# TODO: send the email , string

# browser.close()
