import cv2

image = cv2.imread("sample.jpg")

downsampled = image[::2, ::2]

cv2.imwrite("downsampled.jpg", downsampled)

print("Downsampling completed")