import serial
import cv2
import datetime
import time

ser=serial.Serial()
ser.port='COM3'
ser.baudrate=9600
ser.open()
cap =cv2.VideoCapture(0)

while True:
    print("PLEASE TRIGGER SENSOR TO CAPTURE IMAGE")
    hello=str(ser.readline())
    x=hello.lstrip("b")
    x=x.strip("'")
    x=x.strip("\\r\\n")
    
    if(x=='1'):
        print('triggered')
        ret,frame=cap.read()
        today = datetime.datetime.now()
        t = time.strftime("%I-%M-%S%p")
        file_name = today.strftime('%d-%m-%Y') + '__' + t
        cv2.imwrite('{}.jpg'.format(file_name),frame)
        print("IMAGE CAPTURED")

    else:
        continue