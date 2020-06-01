

import pip

import cv2
import sys
import time
import serial
#import pyserial


#serialPort = serial.Serial("/dev/cu.usbmodem14201", 19200, timeout= 5)
#time.sleep(2)

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))  # float
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))  # float)
widthRatio = 180/width
heightRatio = 180/height
state = False
prev = False
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=30,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    state = False
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        xh = x
        yh = y
        #serialPort.write(str(int(xh * widthRatio)).encode('ascii') + b"x")
        #serialPort.write(str(int(yh * heightRatio)).encode('ascii') + b"y")
        print(str(((xh + w/2) * widthRatio)))
        print(str(((yh + h/2) * heightRatio)))
        state = True


    print(state)
    '''if state == False and state != prev:
        serialPort.write(b"b")
    elif state == False and state != prev:
        serialPort.write(b"a")
    prev = state'''

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
