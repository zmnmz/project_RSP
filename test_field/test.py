from PIL import Image
import pytesseract

import RPi.GPIO as GPIO
import time

# 이미지. 처리.
img =Image.open ('1.png')
text = pytesseract.image_to_string(img, config='')
print (text)
