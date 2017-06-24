import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')

cv2.imshow("Original", image)
cv2.waitKey()
# create kernel 3 X 3

kernel_3_x_3 = np.ones((3, 3), np.float32) / 9  # for normalize we multiply by 1/9
kernel_7_x_7 = np.ones((7, 7), np.float32) / 49
blurring = cv2.filter2D(image, ddepth=-1, kernel=kernel_3_x_3)
more_blurring = cv2.filter2D(image, ddepth=-1, kernel=kernel_7_x_7)
cv2.imshow("Blurring", blurring)
cv2.waitKey()
cv2.imshow("kernel 7 x 7", more_blurring)
cv2.waitKey()

blur_cv = cv2.blur(image, (3, 3))
cv2.imshow("blur_cv", blur_cv)
cv2.waitKey()

blur_cv_gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("blur_cv_gaussian", blur_cv_gaussian)
cv2.waitKey()

blur_cv_median = cv2.medianBlur(image, 5)
cv2.imshow("blur_cv_median ", blur_cv_median)
cv2.waitKey()

blur_cv_bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow("blur_cv_bilateral", blur_cv_bilateral)
cv2.waitKey()


cv2.destroyAllWindows()
