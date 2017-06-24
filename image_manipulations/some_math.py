import cv2
import numpy as np

image = cv2.imread("../images/input.jpg")

# Create a matrix of ones, then multiply it by a scale of 75
# result this will give us a matrix with same shape as original image but all values being 100

M = np.ones(image.shape, dtype="uint8") * 75
img_add = cv2.add(image, M)
cv2.imshow("Mul 75", img_add)
cv2.waitKey()

#  Bitwise Operation

square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -1)
cv2.imshow("Square", square)
cv2.waitKey()

ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("Ellipse", ellipse)
cv2.waitKey()



bit_and = cv2.bitwise_and(square, ellipse)
cv2.imshow("AND", bit_and)
cv2.waitKey()

bit_or = cv2.bitwise_or(square, ellipse)
cv2.imshow("OR", bit_or)
cv2.waitKey()

cv2.destroyAllWindows()
