import cv2
import numpy as np
import time

#faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
cap.set(3,840)
cap.set(4,680)
blink = []
count = 0


while True:
    k=1
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eyeCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (20,20)
    )

    for (x,y,w,h) in eyes:
        k = 0
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
        roi_color = frame[y:y+h, x:x+w]

    if k==1:
        count = count + 1
        print(time.strftime('%H:%M:%S'), count)
        blink.append(time.strftime('%H:%M:%S'))

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Count:'+ str(count),(10,60), font, 1,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow('video', frame)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
        
