import cv2
import numpy as np

img = cv2.imread('Resources/Card.jpg')

width,height = 300,300
pts1 = np.float32([[627,117], [795,308], [454, 554], [290,318]])
pts2 = np.float32([[0,0], [height, 0], [0, width], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgout = cv2.warpPerspective(img,matrix,(width, height))


cv2.imshow('image', img)
cv2.imshow('Output', imgout)
cv2.waitKey(0)
