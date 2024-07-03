from PyPDF2 import PdfMerger

# List of PDF files to merge
all_pdf = ["1.pdf", "2.pdf"]

# Initialize PdfMerger object
merge = PdfMerger()

# Iterate through each PDF file and append it to the merger object
for new_pdf in all_pdf:
    merge.append(new_pdf)

# Write the merged PDF to a new file
with open("3.pdf", "wb") as output_pdf:
    merge.write(output_pdf)

# Close the PdfMerger object
merge.close()
