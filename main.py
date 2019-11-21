from PIL import Image
import pytesseract

import RPi.GPIO as GPIO
import time

# 사용될 모터 핀번호
motor_pin = 0
# 점자
dot=[0,0,0,0,0,0]

# 이미지. 처리.
img =Image.open ('1.png')
text = pytesseract.image_to_string(img, config='')
print (text)

def makeZero(_list):
    for i in range(len(_list)):
        _list[i] = 0

def makeDot(ch, dot):
    makeZero(dot)
    if ch == 'a':
        dot[0]=1
    elif ch == 'b':
        dot[0]=1
        dot[2]=1
    elif ch == 'c':
        dot[0]=1
        dot[1]=1
    elif ch == 'd':
        dot[0]=1
        dot[1]=1
        dot[3]=1
    elif ch == 'e':
        dot[0]=1
        dot[3]=1
    elif ch == 'f':
        dot[0]=1
        dot[1]=1
        dot[2]=1
    elif ch == 'g':
        dot[0]=1
        dot[1]=1
        dot[2]=1
        dot[4]=1
    elif ch == 'h':
        dot[0]=1
        dot[2]=1
        dot[3]=1
    elif ch == 'i':
        dot[1]=1
        dot[2]=1
    elif ch == 'j':
        dot[1]=1
        dot[2]=1
        dot[3]=1
    elif ch == 'k':
        dot[0]=1
        dot[4]=1
    elif ch == 'l':
        dot[0]=1
        dot[2]=1
        dot[4]=1
    elif ch == 'm':
        dot[0]=1
        dot[1]=1
        dot[4]=1
    elif ch == 'n':
        dot[0]=1
        dot[1]=1
        dot[3]=1
        dot[4]=1
    elif ch == 'o':
        dot[0]=1
        dot[3]=1
        dot[4]=1
    elif ch == 'p':
        dot[0]=1
        dot[1]=1
        dot[2]=1
        dot[4]=1
    elif ch == 'q':
        dot[0]=1
        dot[1]=1
        dot[2]=1
        dot[3]=1
        dot[4]=1
    elif ch == 'r':
        dot[0]=1
        dot[2]=1
        dot[3]=1
        dot[4]=1
    elif ch == 's':
        dot[1]=1
        dot[2]=1
        dot[4]=1
    elif ch == 't':
        dot[1]=1
        dot[2]=1
        dot[3]=1
        dot[4]=1
    elif ch == 'u':
        dot[0]=1
        dot[4]=1
        dot[5]=1
    elif ch == 'v':
        dot[0]=1
        dot[2]=1
        dot[4]=1
        dot[5]=1
    elif ch == 'w':
        dot[1]=1
        dot[2]=1
        dot[3]=1
        dot[5]=1
    elif ch == 'x':
        dot[0]=1
        dot[1]=1
        dot[4]=1
        dot[5]=1
    elif ch == 'y':
        dot[0]=1
        dot[1]=1
        dot[3]=1
        dot[4]=1
        dot[5]=1
    elif ch == 'z':
        dot[0]=1
        dot[3]=1
        dot[4]=1
        dot[5]=1
    else:
        makeZero(dot)
    #return dot

# Main Code

# 이미지. 처리.
img =Image.open ('1.png')
text = pytesseract.image_to_string(img, config='')
print (text)
#
text = text.lower()
for ch in text:
    makeDot(ch, dot)
    print(ch+":")
    print(dot)
    time.sleep(1)


