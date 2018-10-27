import numpy as np
import cv2

# Get input from webcam
cap = cv2.VideoCapture(0)

# Continue until user ends program
while (True):
	ret, frame = cap.read()
	frame = cv2.resize(frame, (0, 0), None, .5, .5) # Downsize image
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Convert to HSV
	thresh = cv2.inRange(hsv, (0, 100, 70), (60, 255, 255)) # Threshold to only show skin color
	thresh_3channel = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR) # Convert to 3-channel image
	cv2.imshow('threshold', np.hstack((frame, thresh_3channel))) # Display images side by side
	if cv2.waitKey(1) and 0xFF == ord('q'): # Exit
		break

#Cleanup
cap.release()
cv2.destroyAllWindows()