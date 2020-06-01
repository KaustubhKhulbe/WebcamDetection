import numpy as np
import cv2
import serial
import time
ser = serial.Serial("/dev/cu.usbmodem14201", 19200, timeout= 5)
time.sleep(0.5)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
       cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
       detect=x
       print(detect)

       cv2.imshow('img', img)
       k = cv2.waitKey(30) & 0xff

       if 0 < detect//4 < 100:

        t = detect
        ser.write(bytes(x) + b"x")
        print ("RECIEVED BACK:", repr(ser.read(5000)))

       if k == 27:
            break