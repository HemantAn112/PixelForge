import cv2
import numpy as np

image = cv2.imread("input.jpg")
if image is None:
    raise FileNotFoundError("input.jpg not found")

# Custom sharpening kernel: center is strengthened while neighbours are subtracted.
kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
], dtype=np.float32)

sharpened = cv2.filter2D(image, -1, kernel)
cv2.imwrite("output.png", sharpened)
