import cv2
import numpy as np

cap = cv2.VideoCapture(0)
 
while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    blur = cv2.GaussianBlur(frame,(41,41),0)
    frame_small = cv2.resize(frame, dsize = None, fx = 0.5, fy = 0.5)
    blur_small = cv2.resize(blur, dsize = None, fx = 0.5, fy = 0.5)
    new_image = np.concatenate((frame_small, blur_small), 1)
    cv2.imshow('new_image', new_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()