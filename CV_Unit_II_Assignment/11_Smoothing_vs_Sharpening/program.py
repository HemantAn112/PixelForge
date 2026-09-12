import cv2
import numpy as np

image = cv2.imread("input.jpg")
if image is None:
    raise FileNotFoundError("input.jpg not found")

smooth = cv2.GaussianBlur(image, (5, 5), 0)

kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
], dtype=np.float32)
sharp = cv2.filter2D(image, -1, kernel)

cv2.imwrite("output_smooth.png", smooth)
cv2.imwrite("output_sharp.png", sharp)
