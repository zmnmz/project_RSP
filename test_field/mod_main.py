from PIL import Image
import cv2
import sys
import pytesseract

import RPi.GPIO as GPIO
from time import sleep

from dot import *       # dot.py

# 사용될 모터 핀번호
SVO = [[11,12,13,16,15,18],[19, 22, 21, 24, 23, 26]]
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
    for j in range(2):
        for i in range(6):
            GPIO.setup(SVO[j][i], GPIO.OUT)
            p.append(GPIO.PWM(SVO[j][i], 50))
            p[j][i].start(0)
    for j in range(2):
        for i in range(6):
            p[j][i].ChangeDutyCycle(3)    # 3: 0 || 7.5: 90 || 12: 180
            sleep(1)
    #
    text = text.lower()
    cnt = 0
    for ch in text:
        makeDot(ch, dot)
        print(ch+':')
        print(dot)
        for i in range(6):
            if dot[i] == 1:
                p[cnt][i].ChangeDutyCycle(12)    # 3: 0 || 7.5: 90 || 12: 180
            else:
                p[cnt][i].ChangeDutyCycle(3)
        sleep(1)

        for i in range(6):
            p[cnt][i].ChangeDutyCycle(3)    # 3: 0 || 7.5: 90 || 12: 180
        sleep(1)
        cnt = (cnt + 1) % 2

