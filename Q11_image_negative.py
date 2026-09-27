import cv2

image = cv2.imread("sample.jpg")

negative = 255 - image

cv2.imwrite("negative.jpg", negative)

print("Negative image saved successfully")