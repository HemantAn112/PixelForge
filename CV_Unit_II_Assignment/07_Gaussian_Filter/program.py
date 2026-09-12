import cv2

image = cv2.imread("input.jpg")
if image is None:
    raise FileNotFoundError("input.jpg not found")


smoothed = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imwrite("output.png", smoothed)
