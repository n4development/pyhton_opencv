import cv2
import numpy as np

def sketch(frame):

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # clean Image using Gaussian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Canny
    canny_edge = cv2.Canny(img_gray_blur, 10, 70)

    # threshold  bitwise
    ret, mask = cv2.threshold(canny_edge, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Live Sketcher", sketch(frame))
    if cv2.waitKey(1) == 13:  # Enter Key
        break

cap.release()
cv2.destroyAllWindows()
