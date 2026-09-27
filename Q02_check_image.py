import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Check whether image was loaded successfully
if img is None:
    print("Error: Image could not be loaded. Please check the file path.")
else:
    print("Image loaded successfully.")