import os,io
from GoogleVisionAPI_ReadingIMG import *
#from PIL import Image
import cv2
import numpy as np
from primesense import _openni2 as c_api
from primesense import openni2
import sys
#import pytesseract

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
        # GPIO Setting
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        
        # Button Setting
        GPIO.setup(Button_pin, GPIO.IN)
        
        # Motor setup
        for i in range(6):
            GPIO.setup(SVO[i], GPIO.OUT)
            p.append(GPIO.PWM(SVO[i], 50))
            p[i].start(1)
        
        # Camera Setting
        dev = openni2.Device
        try:
            openni2.initialize()
            dev = openni2.Device.open_any()
            print(dev.get_sensor_info(openni2.SENSOR_DEPTH))
        except (RuntimeError, TypeError, NameError):
            print(RuntimeError, TypeError, NameError)
        depth_stream = dev.create_depth_stream()
        color_stream = dev.create_color_stream()
        depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat=c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM,
                                                       resolutionX=640,
                                                       resolutionY=480,
                                                       fps=30))
        color_stream.set_video_mode(c_api.OniVideoMode(pixelFormat=c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888,
                                                       resolutionX=640,
                                                       resolutionY=480,
                                                       fps=30))
        depth_stream.start()
        color_stream.start()
        # Start Loop
        while True:
            print('Waiting for INPUT...')
            while(True):
                button = GPIO.input(Button_pin)
                if button == True:
                    print("Grab IMG from Camera...")
                    break;
        #while input() == 'a':
            frame_depth = depth_stream.read_frame()
            frame_color = color_stream.read_frame()

            frame_depth_data = frame_depth.get_buffer_as_uint16()
            frame_color_data = frame_color.get_buffer_as_uint8()

            depth_array = np.ndarray((frame_depth.height, frame_depth.width), dtype=np.uint16, buffer=frame_depth_data)
            color_array = np.ndarray((frame_color.height, frame_color.width, 3), dtype=np.uint8, buffer=frame_color_data)
            color_array = cv2.cvtColor(color_array, cv2.COLOR_BGR2RGB)
            
            color_array = cv2.flip(color_array, 1)
            #cv2.imshow('Depth', depth_array)
            #cv2.imshow('Color', color_array)
            
            is_success, im_buf_arr = cv2.imencode('.png', color_array)
            byte_im = im_buf_arr.tobytes()

            content = byte_im
            # Recognize text using CV
            '''
            im = cv2.imread(imPath, cv2.IMREAD_COLOR)
            text = pytesseract.image_to_string(im, config='')
            print (text)
            '''
            # Recognize text using Google Cloud Vision-API
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
            '''
            file_name = os.path.join(
                os.path.dirname(__file__),
                'Hello_world.png')
            '''
            print("Detect TEXT using google cloud API...")
            texts = detect_text('', content)
            
            if (len(texts) > 0):
                pass
            else:
                print('Can not find any TEXT!')
                continue

            print(texts[0].description)
            text = texts[0].description
            
            # Init SVO
            for i in range(len(p)):
                p[i].ChangeDutyCycle(3)
            sleep(1)

            for i in range(6):
                p[i].ChangeDutyCycle(SVO_val[i])    # 3: 0 || 7.5: 90 || 12: 180
                print(str(i)+' : '+str(SVO_val[i]))

            # Loop in text
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
                sleep(0.5)
                
                while True:
                    button = GPIO.input(Button_pin)
                    if button == True:
                        break;
                
            for i in range(len(p)):
                p[i].ChangeDutyCycle(3)
            sleep(0.5)

    except KeyboardInterrupt:
        # QUIT Camera
        depth_stream.stop()
        color_stream.stop()
        openni2.unload()
        
        # QUIT SVO
        for i in range(len(p)):
            p[i].ChangeDutyCycle(3)
        sleep(1)
        print("GPIO.stop() called!")
        for i in range(len(p)):
            p[i].stop()
        print("GPIO.cleanup() called!")
        GPIO.cleanup()

