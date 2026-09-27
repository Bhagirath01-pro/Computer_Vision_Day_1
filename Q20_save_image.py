import cv2

image = cv2.imread("sample.jpg")

cv2.imwrite("saved_image.jpg", image)

print("Image saved successfully")