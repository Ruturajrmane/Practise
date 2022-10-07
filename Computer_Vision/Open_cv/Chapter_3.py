import cv2

img = cv2.imread('Resources/Img.jpg')

print(img.shape)

#Resizing the image
imgre = cv2.resize(img, (500,500))
# Cropping the image in the open cv order of the shape or slice is height, width
imgcrop = img[0:500, 1000:1800]

cv2.imshow('cropped image', imgcrop)
cv2.imshow('Resized Image', imgre)
cv2.waitKey(0)