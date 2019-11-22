from PIL import Image
import cv2
import sys
import pytesseract

import RPi.GPIO as GPIO
from time import sleep

from dot import *       # dot.py

# 사용될 모터 핀번호
SVO = [11,12,13,16,15,18]
p = list()
# 점자
dot=[0,0,0,0,0,0]

# Main Code
if __name__ == '__main__':

    if len(sys.argv) < 2:
        imPath = "1.png"
    else:
        imPath = sys.argv[1]
    #img =Image.open (imPath)
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)
    text = pytesseract.image_to_string(im, config='')
    print (text)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    for i in range(6):
        GPIO.setup(SVO[i], GPIO.OUT)
        p.append(GPIO.PWM(SVO[i], 50))
        p[i].start(0)

    for i in range(6):
        p[i].ChangeDutyCycle(3)    # 3: 0 || 7.5: 90 || 12: 180
        sleep(1)
    #
    text = text.lower()
    for ch in text:
        makeDot(ch, dot)
        print(ch+':')
        print(dot)
        for i in range(6):
            if dot[i] == 1:
                p[i].ChangeDutyCycle(12)    # 3: 0 || 7.5: 90 || 12: 180
            else:
                p[i].ChangeDutyCycle(3)
        sleep(1)

        for i in range(6):
            p[i].ChangeDutyCycle(3)    # 3: 0 || 7.5: 90 || 12: 180
        sleep(1)

