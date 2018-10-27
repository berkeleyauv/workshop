import numpy as np
import cv2

# Get input from webcam
cap = cv2.VideoCapture(0)

# Continue until user ends program
while (True):
	ret, frame = cap.read()
	frame = cv2.resize(frame, (0, 0), None, .5, .5) # Downsize image
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale
	ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) # Threshold image
	im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Find contours of binary image
	cv2.drawContours(frame, contours, -1, (255, 0, 0), 3) # Draw contours on original image
	cv2.imshow('contours', frame) # Display image
	if cv2.waitKey(1) and 0xFF == ord('q'): # Exit
		break

#Cleanup
cap.release()
cv2.destroyAllWindows()