import cv2

image = cv2.imread("sample.jpg")

crop = image[100:300, 100:300]

cv2.imwrite("crop.jpg", crop)

print("Cropped image saved")