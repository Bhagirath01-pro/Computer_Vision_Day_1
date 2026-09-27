import cv2

image = cv2.imread("sample.jpg")

flipped = cv2.flip(image, 1)

cv2.imwrite("flipped.jpg", flipped)

print("Flipped image saved")