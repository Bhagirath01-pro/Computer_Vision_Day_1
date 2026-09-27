import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("sample.jpg")

# Check if image was loaded
if img is None:
    print("Error: Image not found.")
else:
    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display image
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()