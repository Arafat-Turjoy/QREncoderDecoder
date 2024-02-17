#!/usr/bin/env python3
import sys
import qrcode 
import cv2


if(len(sys.argv)<3):
    print("type: make_qrcode 'what you want to encode' 'output filename without extension'")
else:
    user_input = ' '.join(sys.argv[1:len(sys.argv)-1])
    img = qrcode.make(user_input)
    name_of_file = sys.argv[-1]
    if '.'in name_of_file:
       img.save(name_of_file)
    else:
       img.save(name_of_file + ".png")
    
    


    

     
    
