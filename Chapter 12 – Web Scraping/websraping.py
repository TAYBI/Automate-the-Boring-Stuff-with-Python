# # import webbrowser
# # import requests
# # import bs4

# # # Call requests.get() to download the file.
# # # Call open() with 'wb' to create a new file in write binary mode.
# # # Loop over the Response object’s iter_content() method.
# # # Call write() on each iteration to write the content to the file.
# # # Call close() to close the file.


# # # webbrowser.open('https://inventwithpython.com')
# # # Downloading Files from the Web with the requests Module
# # # txtLink = 'https://automatetheboringstuff.com/files/rj.txt'
# # # res = requests.get('')


# # # print(res.text[:250])
# # # print(type(res))
# # # print(res.status_code == requests.codes.ok)
# # # print(res.status_code, requests.codes.ok)


# # # Checking for Errors
# # # res = requests.get('https://automatetheboringstuff.com/som_non_exestiong_url')
# # # try:
# # #     print(res.raise_for_status())
# # # except Exception as exc:
# # #     print('Something went wrong', exc)

# # # Saving Downloaded Files to the Hard Drive

# # # res = requests.get(txtLink)

# # # playFile = open('RomioAndJoliet.txt', 'wb')

# # # for chunk in res.iter_content(100000):
# # #     playFile.write(chunk)

# # # playFile.close()


# # res = requests.get('https://nostarch.com/')

# # try:
# #     res.raise_for_status()
# # except Exception as exc:
# #     print('Something went wrong', exc)

# # noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

# # exampleFile = open('example.html')
# # exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')

# # print(type(noStarchSoup), type(exampleFile))

# # pElements = exampleSoup.select('p')
# # print(pElements[0].getText())
# # # print(pElements)


# # Controlling the Browser with the selenium M
# # from selenium import webdriver

# # browser = webdriver.Firefox()
# # browser.get('https://inventwithpython.com')
# # # try:
# # elem = browser.find_element_by_class_name('col-sm-12')
# # print('Founf <%s> element wityh tahat class name' % (elem))
# # # except:
# # #     print('Was not able to find an element with that name')
# # browser.close()


# # Create a webdriver instance
# # driver = webdriver.Firefox()

# # # Navigate to a webpage
# # driver.get('https://automatetheboringstuff.com')

# # # Find an element with the class 'my-class'
# # element = driver.find_element_by_class_name('top_header')

# # # Do something with the element
# # print(element)

# # # Close the webdriver
# # driver.close()

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://inventwithpython.com')
# linkElem = browser.find_element_by_link_text('Read Online for Free')
# type(linkElem)
# linkElem.click()  # follows the "Read Online for Free" link
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.inventwithpython.com')

elm = browser.find_element(By.CLASS_NAME, "cover-thumb")
print(elm)

browser.close()
