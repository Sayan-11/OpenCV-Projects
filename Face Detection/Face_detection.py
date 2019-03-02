import numpy
import cv2
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)
cap.set(3,840)
cap.set(4,680)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (20,20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(gray, (x,y), (x+w, y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x:w]
        roi_color = frame[y:y+h, x:x+w]
        print(faces)
    cv2.imshow('video', gray)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
        
