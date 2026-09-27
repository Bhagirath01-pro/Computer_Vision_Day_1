import cv2

image = cv2.imread("sample.jpg")

roi = image[100:400, 150:500]

cv2.imwrite("roi.jpg", roi)

print("Rectangular ROI cropped successfully")