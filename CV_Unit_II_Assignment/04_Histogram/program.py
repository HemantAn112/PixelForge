import cv2
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("input.jpg not found")

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
highest = int(hist.argmax())
print("Intensity with highest frequency:", highest)

plt.figure(figsize=(8, 5))
plt.plot(hist)
plt.xlim([0, 256])
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Image Intensity Histogram")
plt.tight_layout()
plt.savefig("output.png", bbox_inches="tight")
plt.close()
