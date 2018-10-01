#!/usr/bin/env python3

"""
This script resizes all the images to A4 size in convert directory and merges them into a single PDF file.

Put all your image files in `/convert` folder before running this script
"""

from os import listdir
from fpdf import FPDF

path = 'convert/'

img_list = listdir(path)
img_list.sort()

pdf = FPDF('P', 'mm', 'A4')

x = 0
y = 0
w = 210
h = 297

for img in img_list:
    pdf.add_page()
    pdf.image(path + img, x, y, w, h)

pdf.output('output.pdf', 'F')