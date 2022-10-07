import cv2
import numpy as np


imgor = cv2.imread('Resources/Img.jpg')
print(imgor.shape)

# Resizing the image
img = cv2.resize(imgor, (500,500))

# As in the cv image order is BGR we are converting from BGR to Gray
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blurring the image
imgblur = cv2.GaussianBlur(img, (7,7), 0)
# Getting the edges with canny
imgcanny = cv2.Canny(img, 150, 200)
# Dilation to get the edges
kernel = np.ones((5,5), np.uint8)
imgdil = cv2.dilate(imgcanny, kernel,iterations = 1) # On changing the iterations the thickness will be increased
# Eroding means decreasing the thickness of the edges
imgerode = cv2.erode(imgdil, kernel, iterations = 1)


cv2.imshow('eroded image', imgerode)
cv2.imshow('Dilated image', imgdil)
cv2.imshow('Blur image', imgblur)
cv2.imshow('Gray Image',  imggray)
cv2.imshow('imgcanny', imgcanny)
cv2.waitKey(0)

