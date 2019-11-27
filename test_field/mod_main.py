##수정부분은 샾 두개로 주석 답니다 참고해주세요. -박준형
##추가사항 구분 
## 1: 모터수 증가로 인한 코드 변경(필수) 
## 2: 모터추가 시 숫자만 변경하면 되도록 수정한 방안(참고)

from PIL import Image
import cv2
import sys
import pytesseract

import RPi.GPIO as GPIO
from time import sleep

from dot import *       # dot.py

# 사용될 모터 핀번호
SVO = [[11,12,13,16,15,18],[19, 22, 21, 24, 23, 26]]        ##추가사항1, 모터 추가에 의한 PIN추가
p = list()
# 점자
dot=[0,0,0,0,0,0]

num_motor = 2   ##추가사항2, 출력 단자 증가로 2뿐만 아니라 더 늘릴수 있기에
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
    for j in range(num_motor):          ##추가사항2
        p.append([])    ##추가사항1, p를 다차원 배열로 만들기위해
        for i in range(6):
            GPIO.setup(SVO[j][i], GPIO.OUT)         ##추가사항1
            p[j].append(GPIO.PWM(SVO[j][i], 50))    ##모터추가에 의한 형식변환
            p[j][i].start(0)                        ##
    for j in range(num_motor):          ##추가사항2
        for i in range(6):
            p[j][i].ChangeDutyCycle(3)    # 3: 0 || 7.5: 90 || 12: 180      ##추가사항1
            sleep(1)
    #
    text = text.lower()
    cnt = 0                             ##추가사항1
    for ch in text:
        makeDot(ch, dot)
        print(ch+':')
        print(dot)
        for i in range(6):
            if dot[i] == 1:
                p[cnt][i].ChangeDutyCycle(12)    # 3: 0 || 7.5: 90 || 12: 180   ##추가사항1
            else:
                p[cnt][i].ChangeDutyCycle(3)                                    ##추가사항1
        sleep(1)

        for i in range(6):
            p[cnt][i].ChangeDutyCycle(3)    # 3: 0 || 7.5: 90 || 12: 180        ##추가사항1
        sleep(1)
        cnt = (cnt + 1) % num_motor                                             ##추가사항1,2 기존의 2개 유지시 cnt = (cnt + 1) % 2 사용

