import  cv2
import numpy as np

img = cv2.imread('./images/dog.jpg')

#Reading RGB Value of the first pixle (0,0)
#B, G, R = img[10,50]
#print B, G, R
#print img.shape

#Reading RGB Values after converting into GrayScale
gry_img = cv2.imread('./images/dog.jpg',0)
print gry_img[10,50]
print gry_img.shape

#Using HSV Color Space
image = cv2.imread('./images/dog.jpg')
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image', hsv_img)
cv2.imshow('Hue Channle', hsv_img[:, :, 0])
cv2.imshow('Saturation Channle', hsv_img[:, :, 1])
cv2.imshow('Value channle', hsv_img[:, :, 2])

cv2.waitKey()
cv2.destroyAllWindows()


#######--Splitting RGB image into three channels--######
B, G, R = cv2.split(img)
print 'B shape:', B.shape
cv2.imshow('Red', R)
cv2.imshow('Green', G)
cv2.imshow('Blue', B)
cv2.waitKey()
cv2.destroyAllWindows()

#Merging all layers again (Red, Green, Blue)
merged = cv2.merge([B,G,R])
cv2.imshow('merged', merged)
cv2.waitKey()
cv2.destroyAllWindows()

#Amplifieng a specific color
#merged = cv2.merge([B+100, G, R])
#cv2.imshow('Merged with +100 Blue Value', merged)

#Creating a Matrix of Zeros
zeros = np.zeros(img.shape[:2], dtype="uint8")
cv2.imshow('red', cv2.merge([zeros, zeros, R]))
cv2.imshow('green', cv2.merge([zeros, G, zeros]))
cv2.imshow('blue', cv2.merge([B, zeros, zeros   ]))
cv2.waitKey()
cv2.destroyAllWindows()

