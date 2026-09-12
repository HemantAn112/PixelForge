import cv2

image = cv2.imread("input.jpg")
if image is None:
    raise FileNotFoundError("input.jpg not found")

filtered = cv2.medianBlur(image, 5)
cv2.imwrite("output.png", filtered)
