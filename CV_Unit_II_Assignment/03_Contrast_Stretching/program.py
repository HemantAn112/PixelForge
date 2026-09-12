import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("input.jpg not found")

old_min = int(image.min())
old_max = int(image.max())
print("Minimum intensity:", old_min)
print("Maximum intensity:", old_max)

if old_max > old_min:
    stretched = ((image.astype(np.float32) - old_min) * 255.0 /
                 (old_max - old_min))
    stretched = np.clip(stretched, 0, 255).astype(np.uint8)
else:
    stretched = image.copy()

cv2.imwrite("output.png", stretched)
