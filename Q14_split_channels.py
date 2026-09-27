import cv2

image = cv2.imread("sample.jpg")

blue, green, red = cv2.split(image)

print("Blue Channel:", blue.shape)
print("Green Channel:", green.shape)
print("Red Channel:", red.shape)