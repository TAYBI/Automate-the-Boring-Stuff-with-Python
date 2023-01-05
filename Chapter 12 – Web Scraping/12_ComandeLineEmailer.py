from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# TODO: takes an email adress and string from the commande line
mail = input('Enter your email: ')
# TODO: check if the imas vailde

text = input('Enter your txtt you want to send: ')

# TODO: log to google account
browser = webdriver.Firefox()
browser.get('https://accounts.google.com/AccountChooser/signinchooser')
emailElement = browser.find_element(By.ID, 'identifierId')

# TODO: send the email , string
emailElement.send_keys(mail)
emailElement.send_keys(Keys.ENTER)

# browser.close()
