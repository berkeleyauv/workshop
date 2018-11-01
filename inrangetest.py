import numpy as np
import cv2
def nothing(x):
	pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('contours')
cv2.createTrackbar('blow','contours',0,255,nothing)
cv2.createTrackbar('glow','contours',0,255,nothing)
cv2.createTrackbar('rlow','contours',0,255,nothing)
cv2.createTrackbar('bhigh','contours',0,255,nothing)
cv2.createTrackbar('ghigh','contours',0,255,nothing)
cv2.createTrackbar('rhigh','contours',0,255,nothing)
cv2.setTrackbarPos('bhigh','contours',255)
cv2.setTrackbarPos('ghigh','contours',255)
cv2.setTrackbarPos('rhigh','contours',255)
while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.75, fy=0.75)
    frame = np.array(np.flip(frame,1))
    #blur = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    hs = cv2.getTrackbarPos('blow','contours')
    ss = cv2.getTrackbarPos('glow','contours')
    vs = cv2.getTrackbarPos('rlow','contours')
    hl = cv2.getTrackbarPos('bhigh','contours')
    sl = cv2.getTrackbarPos('ghigh','contours')
    vl = cv2.getTrackbarPos('rhigh','contours')

    mask = cv2.inRange(hsv, np.array([hs,ss,vs]), np.array([hl,sl,vl]))
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('contours', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#90, 100, 55, 117, 168, 110