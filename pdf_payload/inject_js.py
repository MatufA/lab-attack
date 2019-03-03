import os
import PyPDF2

doc = os.path.join(os.path.dirname(__file__), "test.pdf")
rs = os.path.join(os.path.dirname(__file__), "test_result.pdf")
unmeta = PyPDF2.PdfFileReader(doc, "rb")

meta = PyPDF2.PdfFileWriter()
meta.appendPagesFromReader(unmeta)

meta.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

with open(rs, 'wb') as fp:
    meta.write(fp)
