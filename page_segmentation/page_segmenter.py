from PyPDF2 import PdfFileWriter, PdfFileReader
import pdf2image
import os


def segments_page_pdf_to_pdf():
    resPath = os.path.dirname(os.path.dirname(__file__))
    srcFile = os.path.join(os.path.normpath(resPath),'res','document','bangla_dictionary.pdf')
    inputPdf = PdfFileReader(open(srcFile, "rb"))
    outputDir = os.path.join(resPath,'res','pages')

    for i in range(inputPdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputPdf.getPage(i))
        outputFilename = os.path.join(outputDir, "page%s.pdf" % (i + 1))
        with open(outputFilename, "wb") as outputStream:
            output.write(outputStream)

def convert_pdf_to_image():
    resPath = os.path.dirname(os.path.dirname(__file__))
    srcFile = os.path.join(os.path.normpath(resPath), 'res', 'document', 'bangla_dictionary.pdf')
    print(srcFile)
    outputDir = os.path.join(resPath, 'res', 'page_images')
    pages = pdf2image.convert_from_path(srcFile, 500, output_folder=outputDir, fmt="jpeg")
    i=1
    for page in pages:
        print("Doing page %s" %i)
        page.save(outputDir +"\page%s.jpg" % i, 'JPEG')
        print("Done page %s" %i)
        i= i+1

#segments_page_pdf_to_pdf()
convert_pdf_to_image()


