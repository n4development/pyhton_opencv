import cv2
import numpy as np

image = cv2.imread('../images/bunchofshapes.jpg')
cv2.imshow("Original ", image)
print(image.shape)
board = np.zeros(image.shape, dtype=np.float32)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# canny detect edges

edges = cv2.Canny(gray, 30, 200)

# contours

_, contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("edges", edges)

# draw

cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
cv2.drawContours(board, contours, -1, (255, 0, 0), 2)
cv2.imshow('Image', image)
cv2.imshow("Board", board)



cv2.waitKey(0)
cv2.destroyAllWindows()