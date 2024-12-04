import cv2
import numpy as np

#Path to the image you want to use.
img=cv2.imread('sample.jpg')

#Apply Gaussian blur.
blurred=cv2.GaussianBlur(img,(15,15),0)

#Edge detection using Canny
edges=cv2.Canny(blurred,100,200)

#Convert the Original image from BGR to RGB
rgb_image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Display the images 
cv2.imshow('Original (BGR)',img)
cv2.imshow('Blurred',blurred)
cv2.imshow('Edges',edges)
cv2.imshow('RGB image',rgb_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
