import cv2

image = cv2.imread("sample.jpg")

resized = cv2.resize(image, (300, 300))

cv2.imwrite("resized.jpg", resized)

print("Resized image saved")