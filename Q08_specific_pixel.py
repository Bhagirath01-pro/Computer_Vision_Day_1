import cv2

image = cv2.imread("sample.jpg")

pixel = image[100, 100]

print("Pixel at (100,100):", pixel)