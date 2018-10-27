import numpy as np
import cv2

# Get input from webcam
cap = cv2.VideoCapture(0)

# Continue until user ends program
while (True):
	ret, frame = cap.read()
	frame = cv2.resize(frame, (0, 0), None, .5, .5) # Downsize image
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale
	gray_3channel = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) # Convert to 3-channel image
	cv2.imshow('gray', np.hstack((frame, gray_3channel))) # Display image
	if cv2.waitKey(1) and 0xFF == ord('q'): # Exit
		break

#Cleanup
cap.release()
cv2.destroyAllWindows()