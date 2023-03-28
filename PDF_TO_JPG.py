import fitz

# specify the path of the PDF file
pdf_path = "KHAN.pdf"

# open the PDF
pdf = fitz.open(pdf_path)

# iterate over the pages
for i, page in enumerate(pdf):
    # render the page as a JPEG image
    pix = page.get_pixmap(alpha=False)
    # save the image
    pix._writeIMG(f"page_{i+1}.jpg", format=1)

# close the PDF
print("sucsseful")
pdf.close()
