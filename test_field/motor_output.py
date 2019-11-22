# -*- coding: utf-8 -*-

#선언과 초기화
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

SVO_0 = 11
SVO_1 = 12
SVO_2 = 13
SVO_3 = 16
SVO_4 = 15
SVO_5 = 18

GPIO.setup(SVO_0, GPIO.OUT)
GPIO.setup(SVO_1, GPIO.OUT)
GPIO.setup(SVO_2, GPIO.OUT)
GPIO.setup(SVO_3, GPIO.OUT)
GPIO.setup(SVO_4, GPIO.OUT)
GPIO.setup(SVO_5, GPIO.OUT)

p_0 = GPIO.PWM(11,50)
p_1 = GPIO.PWM(12,50)
p_2 = GPIO.PWM(13,50)
p_3 = GPIO.PWM(16,50)
p_4 = GPIO.PWM(15,50)
p_5 = GPIO.PWM(18,50)

p_0.start(0)
p_1.start(0)
p_2.start(0)
p_3.start(0)
p_4.start(0)
p_5.start(0)

#함수 선언
'''
테스트내용 주석
            p_0 : 양팔,           p_1 : 한팔
3일때      시계,약 170도         시계, 약80도
12        반시계,약 170도
7.5                             반시계, 약80도
모터별로 테스트해서 정확한 수치 구할것

참고용
p_0.ChangeDutyCycle(3)
p_1.ChangeDutyCycle(3)
sleep(1)
p_0.ChangeDutyCycle(12)
sleep(1)
p_1.ChangeDutyCycle(7.5)
sleep(1)
GPIO.cleanup()
'''
'''
#10진수 자연수를 2진수 array로 변환
def conv_data(in_data):
    cnt = 5
    arr = [0,0,0,0,0,0]
    while in_data != 0:
        if in_data%2 == 1:
            arr[cnt] = 1
            in_data = (in_data-1)/2
        else: 
            arr[cnt] = 0
            in_data = in_data/2
        cnt--
return arr
'''
#2진수 array를 통해 모터제어, 이전값과 다를 경우에만 모터 작동, 
#ChangeDutyCycle()함수 내부의 값은 H/W 완성 후 제작을 통해 수정
#함수 이름 그대로 파라미터 pre_data만 줄였을 때 다른함수처럼 작동 가능한지?
def Output_servomoter(pre_data, data):

    if pre_data[0] != data[0]:
        if pre_data[0] == 0 and data[0] == 1:
            p_0.ChangeDutyCycle()
        elif pre_data[0] == 1 and data[0] == 0:
            p_0.ChangeDutyCycle()
    GPIO.cleanup()
