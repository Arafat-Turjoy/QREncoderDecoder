#!/usr/bin/env python3
import sys
import qrcode 
import cv2
# from pyzbar import pyzbar

if(len(sys.argv)<2):
    print("type: scan_qrcode 'qrcode image name'")
else:
    file_to_be_decoded = sys.argv[1]
    d = cv2.QRCodeDetector()
    if '.'in file_to_be_decoded:
        val,points, straight_qrcode = d.detectAndDecode(cv2.imread(file_to_be_decoded))
    else:
        val,points, straight_qrcode = d.detectAndDecode(cv2.imread(file_to_be_decoded + '.png'))
    
    # val = pyzbar.decode(cv2.imread(file_to_be_decoded))
    print(val)



