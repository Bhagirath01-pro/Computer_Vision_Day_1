import cv2

image = cv2.imread("sample.jpg")

height, width = image.shape[:2]

total_pixels = height * width

print("Height:", height)
print("Width:", width)
print("Total Pixels:", total_pixels)