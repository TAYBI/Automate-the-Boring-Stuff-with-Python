from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import random
import string

os.makedirs('pexels', exist_ok=True)

# lanching the driver
url = 'https://www.pexels.com/search/'

# TODO: goes to a photo-sharing
imageSearchValue = input("What kind of photo you want: ")


browser = webdriver.Firefox()
browser.get(url + imageSearchValue)

# searchElement = browser.find_element(By.ID, 'search')
# searchElement.send_keys(imageSearchValue)
# searchElement.send_keys(Keys.ENTER)
# browser.implicitly_wait(5)

Images = browser.find_elements(By.TAG_NAME, 'img')

for image in Images[:-2]:
    imgURL = image.get_attribute('src')
    res = requests.get(imgURL)

    imageName = ''.join(random.choices(string.ascii_lowercase, k=12)) + '.jpeg'
    print('Downloading image:' + imageName + ' ...')
    
    imageFile = open(os.path.join('pexels', imageName), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    # print(image.get_attribute('src'))
    