import cv2
import numpy as np

# For OpenCV2 image display
WINDOW_NAME = 'CockroachBrownTracker'


def track(image):

    # Blur the image to reduce noise
    blur = cv2.GaussianBlur(image, (5, 5), 0)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image for only green colors
    lower_brown = np.array([0, 0, 0])
    upper_brown = np.array([179, 255, 28])
    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_brown, upper_brown)
    # Blur the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)
    b_mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Take the moments to get the centroid
    moments = cv2.moments(b_mask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10'] / m00)
        centroid_y = int(moments['m01'] / m00)

    # Assume no centroid
    ctr = (-1, -1)

    # Use centroid if it exists.
    if centroid_x is not None and centroid_y is not None:
        ctr = (centroid_x, centroid_y)
        # Put black circle in at centroid in image
        #if 202 < centroid_y < 308 and 284 < centroid_x < 468:
        #    print('check how much distance there is between the Wrecker to the Cockroach')
        #    capture.release()
        #    cv2.destroyAllWindows()
        #else:
        cv2.circle(image, ctr, 10, (0, 0, 255))

    # Display full-color image
    cv2.imshow(WINDOW_NAME, image)

    # Force image display, setting centroid to None on ESC key input
    if cv2.waitKey(1) & 0xFF == 27:
        ctr = None

    # Return coordinates of centroid
    return ctr

# Test with input from camera


def find_bug():

    capture = cv2.VideoCapture(0)

    while True:

        okay, image = capture.read()
        #image = cv2.imread('cockroach.jpg')
        if okay:

            track(image)
                

            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            print('Capture failed')
            break


			
			
if __name__ == "__main__":
	find_bug()
	
	
# (284,308)  # Left + Bottom
# (468,281)  # Right + Bottom
# (297,247)  # Left + Up
# (440,202)  # Right + Up
