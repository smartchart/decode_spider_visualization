# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:11:53 2020

@author: Administrator
"""

import pyzbar.pyzbar as pyzbar
from PIL import Image

image = "buctnews.png"
img = Image.open(image)
barcodes = pyzbar.decode(img)
for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print(barcodeData)
