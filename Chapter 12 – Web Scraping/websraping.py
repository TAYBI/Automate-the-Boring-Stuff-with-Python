<<<<<<< HEAD
# import webbrowser
# import requests
# import bs4

# # Call requests.get() to download the file.
# # Call open() with 'wb' to create a new file in write binary mode.
# # Loop over the Response object’s iter_content() method.
# # Call write() on each iteration to write the content to the file.
# # Call close() to close the file.


# # webbrowser.open('https://inventwithpython.com')
# # Downloading Files from the Web with the requests Module
# # txtLink = 'https://automatetheboringstuff.com/files/rj.txt'
# # res = requests.get('')


# # print(res.text[:250])
# # print(type(res))
# # print(res.status_code == requests.codes.ok)
# # print(res.status_code, requests.codes.ok)


# # Checking for Errors
# # res = requests.get('https://automatetheboringstuff.com/som_non_exestiong_url')
# # try:
# #     print(res.raise_for_status())
# # except Exception as exc:
# #     print('Something went wrong', exc)

# # Saving Downloaded Files to the Hard Drive

# # res = requests.get(txtLink)

# # playFile = open('RomioAndJoliet.txt', 'wb')

# # for chunk in res.iter_content(100000):
# #     playFile.write(chunk)

# # playFile.close()


# res = requests.get('https://nostarch.com/')

# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('Something went wrong', exc)

# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')

# print(type(noStarchSoup), type(exampleFile))

# pElements = exampleSoup.select('p')
# print(pElements[0].getText())
# # print(pElements)
=======
import webbrowser

webbrowser.open('https://inventwithpython.com')
>>>>>>> 015ea71ff6ba1e3aabb22d90115bc21f0a0e0107
