import numpy as np
import cv2

# open the camera
cap = cv2.VideoCapture(0)

while True:
        #read the image from the camera
        ret, frame = cap.read()

        # color detection limits
        lB = 0
        lG = 70
        lR = 100
        hB = 30
        hG = 130
        hR = 255
        lowerLimits = np.array([lB, lG, lR])
        upperLimits = np.array([hB, hG, hR])

        # Our operations on the frame come here
        thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
        outimage = cv2.bitwise_and(frame, frame, mask = thresholded)

        # Display the resulting frame
        cv2.imshow('processed',outimage)
        # Quit the program when Q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# When everything done, release the capture
print 'closing program'
cap.release()
cv2.destroyAllWindows()
