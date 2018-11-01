import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    frame = np.array(np.flip(frame,1))
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    ### Color Thresholds
    mask = cv2.inRange(hsv, np.array([90,100,55]), np.array([117,168,110]))
    ### Change Here
    res = cv2.bitwise_and(frame,frame, mask= mask)

    contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours[1]:
    	cnt = max(contours[1], key=lambda x: cv2.minAreaRect(x)[1][0] * cv2.minAreaRect(x)[1][1])
    	rect = cv2.minAreaRect(cnt)
    	boxpts = cv2.boxPoints(rect)
    	box = np.int0(boxpts)
    	cv2.drawContours(frame,[box],0,(0,0,255),5)
    	for corner in boxpts:
        	cv2.circle(frame, (corner[0], corner[1]), 10, (0,0,255), -1)
    	cv2.imshow('contours', np.hstack((frame,res)))
    else:
    	cv2.imshow('contours', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()