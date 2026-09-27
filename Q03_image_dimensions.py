import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Check if image exists
if img is None:
    print("Error: Image not found.")
else:
    height, width, channels = img.shape

    print("Image Height:", height)
    print("Image Width:", width)
    print("Number of Channels:", channels)