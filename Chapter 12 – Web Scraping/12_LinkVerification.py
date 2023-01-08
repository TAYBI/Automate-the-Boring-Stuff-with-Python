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
status4040 = []

for aElem in aElems:
    # print the founded links, and thiere status code
    aElemUrl = str(aElem.get('href'))
    if aElemUrl.startswith('/'):
        aElemUrl = url + aElemUrl
    if aElemUrl.startswith(' '):
        aElemUrl = url + aElemUrl[1:]
    try:
        res = requests.get(aElemUrl)
        # flag any pages that have a 404 status
        if res.status_code == 404:
            status4040.append(aElem)
            continue

        print(f'{res.status_code}: {aElemUrl}')
    except:
        continue

# print the broken links.
print(f'\n> {len(status4040)} broken ' +
      ('link' if len(status4040) <= 1 else 'links') + ' founded')
for brokenLink in status4040:
    print(brokenLink)
print('Done')
