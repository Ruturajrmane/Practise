import cv2
print('imported package')

# Reading the image
def img():
    image = cv2.imread('Resources/Img.jpg')

    cv2.imshow('Output', image)
    cv2.waitKey(0)

# Reading the video
def vdo():
    cap = cv2.VideoCapture('Resources/sample.mp4')
    while True:
        success, img = cap.read()
        cv2.imshow('Video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Reading the video via webcam
def webcam():
    cap = cv2.VideoCapture(0)  # 0 is for the webcam
    cap.set(3, 640)  # 3 is the width
    cap.set(4, 480)  # 4 is the height
    cap.set(10, 100)  # Changing the brittness
    while True:
        success, img = cap.read()
        cv2.imshow('Video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

webcam()