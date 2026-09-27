import cv2

image = cv2.imread("sample.jpg")

image[100, 100] = [0, 0, 255]

print("Pixel modified successfully")