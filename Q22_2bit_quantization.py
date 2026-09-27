import cv2

image = cv2.imread("sample.jpg")

quantized = (image // 64) * 64

cv2.imwrite("2bit_quantized.jpg", quantized)

print("2-bit quantization completed")