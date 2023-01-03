import requests
import os
import bs4


url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    #  Download the page.
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    commicElem = soup.select('#comic img')
    if commicElem == []:
        print('Could\'t find comic image.')
    else:
        # print(commicElem[0].get('src'))
        comicUrl = 'http:' + commicElem[0].get('src')

        # Download the image.
        print(f'Downloading page {comicUrl}...')
        res = requests.get(comicUrl)
        res.raise_for_status()

    # Save the image to ./xkcd.
    imageFilePath = os.path.join('xkcd', os.path.basename(comicUrl))
    # print(imageFilePath)
    imageFile = open(imageFilePath, 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0].get('href')
    url = 'https://xkcd.com' + prevLink

print('Done')
