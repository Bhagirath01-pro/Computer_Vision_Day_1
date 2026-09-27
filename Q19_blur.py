import cv2

image = cv2.imread("sample.jpg")

blur = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imwrite("blur.jpg", blur)

print("Blurred image saved")