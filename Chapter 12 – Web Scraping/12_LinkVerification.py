import requests
import bs4

# take URL of a web page
url = input('type your websile: ')
# url = 'https://www.bdodigital.com'
if not url.startswith('http'):
    url = 'https://' + url

print('Downloading the site...' + url)
res = requests.get(url)
if res.status_code == requests.codes.ok:
    print('ok')

# download every linked page on the page
soup = bs4.BeautifulSoup(res.text, 'html.parser')
aElems = soup.select('a')

for aElem in aElems:
    # flag any pages that have a 404 status
    # print them out as broken links.
    aElemUrl = str(aElem.get('href'))
    if aElemUrl.startswith('/'):
        aElemUrl = url + aElemUrl
    if aElemUrl.startswith(' '):
        aElemUrl = url + aElemUrl[1:]
    try:
        res = requests.get(aElemUrl)
        print(f'{res.status_code}: {aElemUrl}')
    except:
        continue

print('Done')
