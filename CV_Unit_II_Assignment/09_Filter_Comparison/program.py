import cv2

image = cv2.imread("input.jpg")
if image is None:
    raise FileNotFoundError("input.jpg not found")

mean_result = cv2.blur(image, (5, 5))
gaussian_result = cv2.GaussianBlur(image, (5, 5), 0)
median_result = cv2.medianBlur(image, 5)

cv2.imwrite("output_mean.png", mean_result)
cv2.imwrite("output_gaussian.png", gaussian_result)
cv2.imwrite("output_median.png", median_result)
