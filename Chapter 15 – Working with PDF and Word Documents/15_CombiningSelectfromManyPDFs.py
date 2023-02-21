import PyPDF2
import os

# At a high level, here’s what the program will do:

#  X  Find all PDF files in the current working directory.
#  X  Sort the filenames so the PDFs are added in order.
#     Write each page, excluding the first page, of each PDF to the output file.

# In terms of implementation, your code will need to do the following:

#  X  Call os.listdir() to find all the files in the working directory and remove any non-PDF files.
#  X  Call Python’s sort() list method to alphabetize the filenames.
#  X  Create a PdfFileWriter object for the output PDF.
#     Loop over each PDF file, creating a PdfFileReader object for it.
#     Loop over each page (except the first) in each PDF file.
#     Add the pages to the output PDF.
#     Write the output PDF to a file named allminutes.pdf.

# Find All PDF Files
pdfFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfWriter()

# TODO: Loop through all the PDF files.
# TODO: Loop through all the pages (except the first) and add them.
# TODO: Save the resulting PDF to a file.
