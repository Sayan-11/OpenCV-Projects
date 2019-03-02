import numpy
import cv2
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

"""def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        coords.append((x,y))
        print(coords[-1])"""

#60 201 289 145

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    smiles = smileCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (20,20)
    )

    for (x,y,w,h) in smiles:
        sm_ratio = str(round(w/h, 4))
        if float(sm_ratio)<=1.9931:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),1)
            roi_gray = gray[y:y+h, x:x:w]
            roi_color = frame[y:y+h, x:x+w]
    cv2.imshow('video', frame)
    print(x,y,w,h)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
        
