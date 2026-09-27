import cv2

image = cv2.imread("sample.jpg")

rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("rotated.jpg", rotated)

print("Rotated image saved")