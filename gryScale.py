
import cv2

########-Testing Gray Scale Functionality-##########

#load input image
input = cv2.imread('.\images\dog.jpg')
cv2.imshow('Original',input)
cv2.waitKey()

#use cvtColor to convert to grayScale
gray_img = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

#show output image after converting
cv2.imshow('GrayScale Image', gray_img)
cv2.waitKey()
cv2.destroyAllWindows()

#Another Faster Method is to get gray scale image
#the idea is when you put '0' as a second argument
img = cv2.imread('./images/dog.jpg',0)
cv2.imshow('GrayScale II', img)
cv2.waitKey()
cv2.destroyAllWindows()