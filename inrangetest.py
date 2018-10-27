import numpy as np
import cv2
def nothing(x):
	pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('contours')
cv2.createTrackbar('hues','contours',0,255,nothing)
cv2.createTrackbar('sats','contours',0,255,nothing)
cv2.createTrackbar('vals','contours',0,255,nothing)
cv2.createTrackbar('huel','contours',0,255,nothing)
cv2.createTrackbar('satl','contours',0,255,nothing)
cv2.createTrackbar('vall','contours',0,255,nothing)
while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.75, fy=0.75)
    frame = np.array(np.flip(frame,1))
    #blur = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    hs = cv2.getTrackbarPos('hues','contours')
    ss = cv2.getTrackbarPos('sats','contours')
    vs = cv2.getTrackbarPos('vals','contours')
    hl = cv2.getTrackbarPos('huel','contours')
    sl = cv2.getTrackbarPos('satl','contours')
    vl = cv2.getTrackbarPos('vall','contours')

    mask = cv2.inRange(hsv, np.array([hs,ss,vs]), np.array([hl,sl,vl]))
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('contours', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()