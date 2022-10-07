import cv2
import numpy as np

imgor = cv2.imread('Resources/Img.jpg')

img = cv2.resize(imgor, (300,300))

imgHor = np.hstack((img,img))
imgVar = np.vstack((img,img))

cv2.imshow('Image', img)
cv2.imshow('Vertical_stack', imgVar)
cv2.imshow('Horintal_stack', imgHor)
cv2.waitKey(0)