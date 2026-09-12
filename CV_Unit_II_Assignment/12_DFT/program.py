import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("input.jpg not found")

image_float = np.float32(image)
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)
shifted = np.fft.fftshift(dft)

print("Original image shape:", image.shape)
print("DFT result shape:", dft.shape)
print("Shifted DFT shape:", shifted.shape)

magnitude = cv2.magnitude(shifted[:, :, 0], shifted[:, :, 1])
spectrum = 20 * np.log(magnitude + 1)
spectrum = cv2.normalize(spectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
cv2.imwrite("output.png", spectrum)
