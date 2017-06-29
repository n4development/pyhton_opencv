import cv2
import numpy as np

image = cv2.imread('../images/shapes.jpg')
cv2.imshow("Original ", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find edges using canny
min_threshold = 30
max_threshold = 200
edges = cv2.Canny(gray, min_threshold, max_threshold)
cv2.imshow("Canny edges ", edges)

# Finding contours
# use a copy of the image since findContours alter the image
# RETR_LIST -> all contours
# RETR_COMP ->  all in 2 level hierarchy
# RETR_TREE -> all in full hierarchy
# RETR_EXTERNAL -> outer contours only

_, contours, hierarchy  = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("Canny edges after Contouring", edges)
print("Number of contours found {count}".format(count=len(contours)))


# Draw all contours use -1 to draw all

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow("Contours", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
