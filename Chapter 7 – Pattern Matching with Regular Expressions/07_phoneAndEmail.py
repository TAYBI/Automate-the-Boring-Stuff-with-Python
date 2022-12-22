import pyperclip
import re


phoneRegex = re.compile(r'''(
  (\d{3}|\(\d{3}\))?    # area Code
  (\s|-|\.)?                    # area seperaor
  (\d{3})                         # area 3 degit
  (\s|-|\.)?                    # area seperaor
  (\d{4})                      #area 4 degit
)''', re.VERBOSE)


emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)


# finding phone numbers and email addresses on the clipboard.
text = str(pyperclip.paste())
matches = []

# mo = phoneRegex.findall(text)
# print(mo)

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    # if groups[8] != '':
    #     phoneNum += ' x' + groups[8]

    if len(phoneNum) != 12:
        continue
    matches.append(phoneNum)


for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))

else:
    print('No phone numbers or email addresses found')
