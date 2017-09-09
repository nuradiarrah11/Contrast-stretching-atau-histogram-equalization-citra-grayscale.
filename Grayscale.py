import cv2

image = cv2.imread('MyPic.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('MyPic1.jpg', gray)
