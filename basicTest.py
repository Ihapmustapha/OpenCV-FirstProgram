import cv2
import numpy as np

# np could be anything, for example could be x

# Loading image using imread
input = cv2.imread('./images/dog.jpg')

# to show the image we use imshow it takes two parameters
# first one a message to show on the window
# second one the image variable we've loaded the image into
cv2.imshow('Hellow World', input)

# to prevent the window from closing immediatly
cv2.waitKey(0)

# to close all open windows
cv2.destroyAllWindows()

# to get image dimensions (height, width, RGB)
print input.shape
# we use int to convert the value from xx L to xx as an intger
print "Height of the image: ", int(input.shape[0]), " Pixels"
print "width of the image: ", int(input.shape[1]), "Pixels"

# to specify an output file with name and the image to be saved in
cv2.imwrite('output.jpg', input)

