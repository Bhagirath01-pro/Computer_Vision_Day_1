import cv2

image = cv2.imread("sample.jpg")

rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("rotate_90.jpg", rotated)

print("Image rotated 90 degrees clockwise")