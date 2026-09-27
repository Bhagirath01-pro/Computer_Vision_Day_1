import cv2

image = cv2.imread("sample.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray.jpg", gray)

print("Grayscale image saved successfully")