import cv2
import serial
import numpy as np

ser = serial.Serial('COM12', 9600, timeout= 1)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

print(ser.writable())
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame,(1280,820),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv_frame, low_red,high_red)
    contours = cv2.findContours(red_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    contours = sorted(contours,key = lambda x: cv2.contourArea(x), reverse= True)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x,y), (x+ w,y+h), (0, 255, 0), 2)
        x_medium = (x + x + w) /2
        y_medium = (y+ y + h) / 2
        cv2.putText(frame,str(x_medium),(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        # cv2.putText(frame,str(y_medium),(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        if x_medium <500:
            ser.write(b'2\n')
            print('left')
        elif x_medium >800:
            ser.write(b'1\n')
            print('right')
        else:
            ser.write(b'3\n')
            print('stop')
        break
    # cv2.line(frame,(x_medium,0),(x_medium,480),(255,0,0),2)
    # cv2.line(frame,(0,y_medium),(620,y_medium),(0,0,255),2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
ser.write(b'2')