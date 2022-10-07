import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)
# np.uint8 gives the 8 bit values i.e 2^8 = 256 (0 to 255)
# img[:] = 55, 30, 60 # Adding the colours

cv2.line(img, (0,0), (300,300),(0,255,0), 3) # BGR is the sequence for color
cv2.rectangle(img, (0,0), (300,300), (0,0,255), 2)
cv2.circle(img, (250,250), 50, (255,0,0), 3)

# Inserting the letters onto the image
cv2.putText(img, "Shivchatrapati", (100,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0),1)


cv2.imshow('Image', img)
cv2.waitKey(0)