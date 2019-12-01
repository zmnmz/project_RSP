from PIL import Image
import cv2
import sys
import pytesseract

import RPi.GPIO as GPIO
from time import sleep

from dot import *       # dot.py

# 사용될 모터 핀번호
SVO = [11, 12, 13, 16, 23, 18]
SVO_val = [6.5, 6.5, 6.5, 6.5, 6.5, 7.5]
p = list()
# 점자
dot=[0,0,0,0,0,0]

Button_pin = 4

# Main Code
if __name__ == '__main__':
    
    try:
        if len(sys.argv) < 2:
            imPath = "3.png"
        else:
          imPath = sys.argv[1]
        #img =Image.open (imPath)
        im = cv2.imread(imPath, cv2.IMREAD_COLOR)
        text = pytesseract.image_to_string(im, config='')
        print (text)

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        
        # Button setup
        GPIO.setup(Button_pin, GPIO.IN)
        
        # Motor setup
        for i in range(6):
            GPIO.setup(SVO[i], GPIO.OUT)
            p.append(GPIO.PWM(SVO[i], 50))
            p[i].start(1)

        for i in range(len(p)):
            p[i].ChangeDutyCycle(3)
        sleep(1)

        for i in range(6):
            p[i].ChangeDutyCycle(SVO_val[i])    # 3: 0 || 7.5: 90 || 12: 180
            print(str(i)+' : '+str(SVO_val[i]))

        #
        text = text.lower()
        for ch in text:
            makeDot(ch, dot)
            print(ch+':')
            print(dot)

            for i in range(6):
                if dot[i] >= 1:
                    p[i].ChangeDutyCycle(3)
                else:
                    p[i].ChangeDutyCycle(SVO_val[i])    # 3: 0 || 7.5: 90 || 12: 180
            sleep(1)
            
            while True:
                button = GPIO.input(Button_pin)
                if button == True:
                    break;
            
        for i in range(len(p)):
            p[i].ChangeDutyCycle(3)
        sleep(1)

    except KeyboardInterrupt:
        for i in range(len(p)):
            p[i].ChangeDutyCycle(3)
        sleep(1)
        print("GPIO.stop() called!")
        for i in range(len(p)):
            p[i].stop()
        print("GPIO.cleanup() called!")
        GPIO.cleanup()

