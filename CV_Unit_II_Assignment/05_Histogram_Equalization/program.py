import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("input.jpg not found")

equalized = cv2.equalizeHist(image)
cv2.imwrite("output.png", equalized)

hist_before = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_after = cv2.calcHist([equalized], [0], None, [256], [0, 256])

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(hist_before)
plt.title("Before Equalization")
plt.xlim([0, 256])

plt.subplot(1, 2, 2)
plt.plot(hist_after)
plt.title("After Equalization")
plt.xlim([0, 256])

plt.tight_layout()
plt.savefig("histogram_comparison.png", bbox_inches="tight")
plt.close()
