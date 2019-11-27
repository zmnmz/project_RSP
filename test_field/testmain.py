from PIL import Image
import cv2
import sys


from testdot import *       # dot.py #import RPi.GPIO as GPIO & pytesseract & sleep

# 사용될 모터 핀번호
SVO = [11,12,13,16,15,18]
p = [pros]

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
    text = text.lower()

    setup(SVO,p)

    setMotors(p,3,1) #p,ChangeDutyCycle(3),sleep(1)
    
    printDot(p,text,0) #p, text, 출력할 글자 수 = 1 (0 무제한), 글자 간격마다 sleep할 시간 = 1

    setMotors(p,3,1)

