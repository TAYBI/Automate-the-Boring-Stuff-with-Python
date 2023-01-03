import requests
import sys
import webbrowser
import bs4

print('searching...')

# res = requests.get('https://pypi.org/search/?q=mail' + ' '.join(sys.argv[1:]))
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('Something went wrong,' + exc)

# Retrieve top search result links.
# soup = bs4.BeautifulSoup(res.text, 'html.parser')

# fixing Code
url = "https://pypi.org/search/"
params = {"q": ' '.join(sys.argv[1:])}  # add "hl":"en" to get english results
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}
soup = bs4.BeautifulSoup(
    requests.get(url, params=params, headers=headers).content, "html.parser"
)

linkElements = soup.select('.package-snippet')
# print(linkElements)
# Open a browser tab for each result.
nbrOpen = min(5, len(linkElements))
for i in range(nbrOpen):
    urlOpen = 'https://pypi.org' + linkElements[i].get('href')
    print('Openning..' + urlOpen)
    webbrowser.open(urlOpen)
