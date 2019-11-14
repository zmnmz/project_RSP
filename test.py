from PIL import Image
import pytesseract

import RPi.GPIO as GPIO
import time

# 이미지. 처리.
img =Image.open ('1.png')
text = pytesseract.image_to_string(img, config='')
print (text)

GPIO.setmode(GPIO.BOARD)
Act1 = 11
GPIO.setup(Act1, GPIO.OUT, initial = GPIO.LOW)

while (True):
    GPIO.output(Act1, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(Act1, GPIO.LOW)
    time.sleep(3)


