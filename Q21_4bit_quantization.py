import cv2

image = cv2.imread("sample.jpg")

quantized = (image // 16) * 16

cv2.imwrite("4bit_quantized.jpg", quantized)

print("4-bit quantization completed")