"""
We use transformations to correct distortions or perspective issues.

Transformations Types :
* Affine
* Non-Affine

"""

import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')

height, width = image.shape[:2]
quarter_height = height * 0.25
quarter_width = width * 0.25

"""
Translation

#     |   1   0   Tx  |
# T = |               |
#     |   0   1   Ty  |

"""
T = np.float32([
    [1, 0, quarter_width],
    [0, 1, quarter_height]
])

img_translation = cv2.warpAffine(image, T, (width, height))
cv2.imshow("Translation", img_translation)
cv2.waitKey()
cv2.destroyAllWindows()

"""
Rotation

#     |   cos ø     - sin ø |
# R = |                     |
#     |   sin ø       cos ø |

"""

center_of_rotation_x = width / 2
center_of_rotation_y = height / 2
angle = 90

rotation_matrix = cv2.getRotationMatrix2D((center_of_rotation_x, center_of_rotation_y), angle=angle, scale=1)
img_rotate = cv2.warpAffine(image, rotation_matrix, (width, height))
cv2.imshow("Rotate", img_rotate)
cv2.waitKey()
cv2.destroyAllWindows()

"""

Re-sizing and scaling

"""

image_scaling_down = cv2.resize(image, None, fx=0.75, fy=0.75)  # scaling from x and y range 75% from the original one.
cv2.imshow("Down", image_scaling_down)

image_scaling_up = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # scaling double size
cv2.imshow("Double", image_scaling_up)

image_scaling_ex = cv2.resize(image, (900, 400), interpolation=cv2.INTER_AREA)
cv2.imshow("scaling 3", image_scaling_ex)

cv2.waitKey()
cv2.destroyAllWindows()

"""
Cropping Image
"""

start_y, start_x = int(height * .25), int(width * .25)
end_y, end_x = int(height * .75), int(width * .75)

cropped_img = image[start_x:end_x, start_y: end_y]
cv2.imshow("Cropped", cropped_img)
cv2.waitKey()
cv2.destroyAllWindows()

