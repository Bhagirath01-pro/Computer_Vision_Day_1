import cv2

image = cv2.imread("sample.jpg")

channels = image.shape[2]

print("Number of Channels:", channels)