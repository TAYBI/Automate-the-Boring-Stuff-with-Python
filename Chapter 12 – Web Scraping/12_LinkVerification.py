from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import bs4

# TODO: take URL of a web page
# url = input('type your websile: ')
url = 'https://www.bdodigital.com'
if not url.startswith('http'):
    url = 'https://' + url

print('Downloading the site...' + url)
res = requests.get(url)
if res.status_code == requests.codes.ok:
    print('ok')

# TODO: download every linked page on the page
soup = bs4.BeautifulSoup(res.text, 'html.parser')
aElems = soup.select('a')
for aElem in aElems:
    print(aElem.get('href'))
# TODO: flag any pages that have a 404 status
# TODO: print them out as broken links.
