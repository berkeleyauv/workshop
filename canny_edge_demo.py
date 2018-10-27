import numpy as np
import cv2

# Get input from webcam
cap = cv2.VideoCapture(0)

# Continue until user ends program
while (True):
	ret, frame = cap.read()
	frame = cv2.resize(frame, (0, 0), None, .5, .5) #Downsize image
	edges = cv2.Canny(frame, 100, 150) # Find edges
	edges_3channel = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR) # Convert to 3-channel image
	cv2.imshow('edges', np.hstack((frame, edges_3channel))) # Display image
	if cv2.waitKey(1) and 0xFF == ord('q'): # Exit
		break

#Cleanup
cap.release()
cv2.destroyAllWindows()