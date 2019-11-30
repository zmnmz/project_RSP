import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

SVO_0 = 12
SVO_1 = 16

GPIO.setup(SVO_0, GPIO.OUT)
GPIO.setup(SVO_1, GPIO.OUT)

p_0 = GPIO.PWM(12,50)
p_1 = GPIO.PWM(16,50)

# 3: 0 || 7.5: 90 || 12: 180

p_0.start(0)
#p_1.start(0)
p_1.ChangeDutyCycle(3)
sleep(1)
p_1.ChangeDutyCycle(3)
sleep(1)
p_1.ChangeDutyCycle(3)
sleep(1)

GPIO.cleanup()
