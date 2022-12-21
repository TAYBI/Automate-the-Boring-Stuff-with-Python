import pyperclip
import re


phoneRegex = re.compile(r'''(
  (\d{3}|(\d{3}))?                # area Code
  (\s|-|\.)?                      # area seperaor
  \d{3}                           # area 3 degit
  (\s|-|\.)                       # area seperaor
  \d{4}                           # area 4 degit
  (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)


emailRegex = re.compile(r'''
  [a-zA-Z-0-9_.+-%]+
  @
  [a-zA-Z-0-9_.+-]+
  \.
  [a-zA-Z]{2,7}
''', re.VERBOSE)


# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.
