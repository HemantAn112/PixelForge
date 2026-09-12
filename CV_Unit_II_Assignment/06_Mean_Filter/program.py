import cv2

image = cv2.imread("input.jpg")
if image is None:
    raise FileNotFoundError("input.jpg not found")

# Tested with 3x3 first; final required output uses the larger 7x7 kernel.
small = cv2.blur(image, (3, 3))
large = cv2.blur(image, (7, 7))

cv2.imwrite("output.png", large)
