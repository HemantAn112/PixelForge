import cv2

image = cv2.imread("input.jpg")
if image is None:
    raise FileNotFoundError("input.jpg not found")

increase = 60
bright = cv2.add(image, increase)

y, x = 100, 100
print("Pixel before:", image[y, x])
print("Pixel after :", bright[y, x])

cv2.imwrite("output.png", bright)
