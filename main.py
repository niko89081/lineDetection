#https://stackoverflow.com/questions/45322630/how-to-detect-lines-in-opencv
import cv2 as cv
import numpy as np
import math

img = cv.imread("image6.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.blur(gray, (5,5))
edges = cv.Canny(blur, 300, 450, 0, apertureSize=3)
lines = cv.HoughLines(edges, 1, np.pi / 180, 150, None, 0, 0)
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv.line(img, pt1, pt2, (100, 0, 69), 3, cv.LINE_AA)

cv.imshow("HELLLOE", img)
cv.waitKey(0)
cv.destroyAllWindows()
