
from pathlib import Path
import random
import shutil
import re
import os

folder = Path.cwd() / 'FileDates'
# Path.mkdir(folder)

# Create a code to generate all the anerican files
# You can uncoment this code if you want to generate the files

# for i in range(100):
#   file = open(
#       folder / f'{random.randint(1,12)}-{random.randint(1,31)}-{random.randint(1900,2100)}.txt', 'w')
#   file.close()


datePattern = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)\d)-
((19|20)\d\d)
(.*?)$
""", re.VERBOSE)

# Loop over the files in the working directory.


for amerFilename in os.listdir(folder):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.

    euroFilename = f'{beforePart}{dayPart}-{monthPart}-{yearPart}{afterPart}'

    # Get the full, absolute file paths.

    absWorkingDir = os.path.abspath(folder)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    amerFilename = os.path.join(absWorkingDir, amerFilename)

    # print(absWorkingDir)
    # print(amerFilename, '------>', euroFilename)

    # Rename the files.
    # shutil.move(amerFilename, euroFilename)
