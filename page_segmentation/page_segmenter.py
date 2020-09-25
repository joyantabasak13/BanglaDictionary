from PyPDF2 import PdfFileWriter, PdfFileReader
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

segments_page_pdf_to_pdf()