import RPi.GPIO as GPIO
import pytesseract
from time import sleep

def setup(SVO,p):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
    for i in range(len(SVO)):
        GPIO.setup(SVO[i], GPIO.OUT)
        p.append(GPIO.PWM(SVO[i], 50))
        p[i].start(0)
    print('setup')

#텍스트 진행도 progress
progress = 0

def printDot(p,originalText,number = 1,t = 1):
    global progress
    dot=[0,0,0,0,0,0]
    
    text = originalText[progress:] #progress부터 시작

    n = 0
    for ch in text:
        makeDot(ch, dot)
        print(ch+':')
        print(dot)
        for i in p:
            if dot[i] == 1:
                i.ChangeDutyCycle(12)    # 3: 0 || 7.5: 90 || 12: 180
            else:
                i.ChangeDutyCycle(3)
            sleep(t)
            
        n += 1
        #number의 수만큼 출력하고 종료, (number=0 이면 제한없음)
        if n == number:
            return progress += number

def setMotors(p,n,t=0):
    for i in p:
        i.ChangeDutyCycle(n)
    sleep(t)
        
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
