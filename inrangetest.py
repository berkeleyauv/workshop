import numpy as np
import cv2
def nothing(x):
	pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('contours')
cv2.createTrackbar('hlow','contours',0,255,nothing)
cv2.createTrackbar('slow','contours',0,255,nothing)
cv2.createTrackbar('vlow','contours',0,255,nothing)
cv2.createTrackbar('hhigh','contours',0,255,nothing)
cv2.createTrackbar('shigh','contours',0,255,nothing)
cv2.createTrackbar('vhigh','contours',0,255,nothing)
cv2.setTrackbarPos('hhigh','contours',255)
cv2.setTrackbarPos('shigh','contours',255)
cv2.setTrackbarPos('vhigh','contours',255)
while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.75, fy=0.75)
    frame = np.array(np.flip(frame,1))
    #blur = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    hs = cv2.getTrackbarPos('hlow','contours')
    ss = cv2.getTrackbarPos('slow','contours')
    vs = cv2.getTrackbarPos('vlow','contours')
    hl = cv2.getTrackbarPos('hhigh','contours')
    sl = cv2.getTrackbarPos('shigh','contours')
    vl = cv2.getTrackbarPos('vhigh','contours')

    mask = cv2.inRange(hsv, np.array([hs,ss,vs]), np.array([hl,sl,vl]))
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('contours', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#90, 100, 55, 117, 168, 110