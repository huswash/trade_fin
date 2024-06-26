from pdfquery import PDFQuery

# pdf = PDFQuery('FXD2-2016-2IIFB1-2016-9.pdf')
# pdf.load()

# Use CSS-like selectors to locate the elements
# text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
# text = [t.text for t in text_elements]

# customer_name = pdf.pq('LTTextLineHorizontal:in_bbox("8315,680,395,700")').text()

# print(customer_name)
# 89.904, 231.57, 101.990, 265.7

# print(text)
# label = pdf.pq('LTTextLineHorizontal:contains("Performance Rate")')
# left_corner = float(label.attr('x0'))
# bottom_corner = float(label.attr('y0'))
# name = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner-30, left_corner+150, bottom_corner)).text()
# print(name)

# pdf.extract( [
#          ('with_parent','LTPage[pageid=1]'),
#          ('with_formatter', 'text'),

#          ('Total Amount Accepted (Kshs. M)', 'LTTextLineHorizontal:in_bbox("315,680,395,700")'),
#          ('Performance Rate', 'LTTextLineHorizontal:in_bbox("170,650,220,680")')
#      ])

import tabula
from pdfminer.high_level import extract_pages, extract_text
import re

tables = tabula.read_pdf("FXD2-2016-2IIFB1-2016-9.pdf", pages="all")
print(type(tables[0]))

text = extract_text("FXD2-2016-2IIFB1-2016-9.pdf")
# pattern = re.compile(r"\b(?:FXD|IFB\d*)\s\d+/\d{4}/\d+\b")
pattern = re.compile(r"FXD \d{1,2}/\d{4}/\d{1,2}|IFB\d{1,2}/\d{4}/\d{1,2}")
matches = pattern.findall(text)

print(matches)
# print(text)
# pattern = re.compile(r"[a-zA-Z\d]+\s{1}")