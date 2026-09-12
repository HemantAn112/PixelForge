import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("input.jpg not found")

rows, cols = image.shape
crow, ccol = rows // 2, cols // 2

dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
shifted = np.fft.fftshift(dft)

# Circular high-pass mask: remove the central low-frequency region.
radius = min(rows, cols) // 12
mask = np.ones((rows, cols, 2), np.float32)
cv2.circle(mask, (ccol, crow), radius, (0, 0), -1)

filtered_shifted = shifted * mask
unshifted = np.fft.ifftshift(filtered_shifted)
reconstructed = cv2.idft(unshifted, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
reconstructed = cv2.normalize(reconstructed, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

cv2.imwrite("output.png", reconstructed)
