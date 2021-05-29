# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:11:53 2020

@author: Administrator
"""


import pyzbar.pyzbar as pyzbar
from PIL import Image
from MyQR import myqr
image = "buctnews.png"
img = Image.open(image)
barcodes = pyzbar.decode(img)
for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print(barcodeData)
myqr.run(
    words=barcodeData,
    colorized=True, # 显示彩色
    picture='03.gif',    # 风格图片
)