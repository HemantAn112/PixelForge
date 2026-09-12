import cv2

image = cv2.imread("input.jpg")
if image is None:
    raise FileNotFoundError("input.jpg not found")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Original image shape:", image.shape)
print("Grayscale image shape:", gray.shape)
print("Height:", image.shape[0])
print("Width:", image.shape[1])

cv2.imwrite("output.png", gray)
