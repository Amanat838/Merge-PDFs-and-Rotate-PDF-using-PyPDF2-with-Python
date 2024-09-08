import PyPDF2

with open("your pdf here", "rb") as file:

    reader = PyPDF2.PdfReader(file)
    no_of_pages = len(reader.pages)
    print(no_of_pages)

    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("rotated", "wb") as output:
        writer.write(output)

merger = PyPDF2.PdfMerger()
file_names = ["your first pdf", "your second pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")
