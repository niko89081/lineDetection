#https://stackoverflow.com/questions/45322630/how-to-detect-lines-in-opencv
import cv2 as cv
import numpy as np

def averager(lines):
        
img = cv.imread("IMG_1696.jpg")
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv.resize(img, dim, interpolation= cv.INTER_AREA)
grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("imgmg", img)
cv.waitKey(0)

dst = cv.Canny(grayed, 575, 600)
cv.imshow("dst", dst)
blurred = cv.blur(dst, (3, 3))
cv.imshow("blured lines", blurred)
line1 = cv.HoughLinesP(blurred, 2, np.pi / 180, 150, None, 275, 0)
print(len(line1))
if line1 is not None:
        for i in range(len(line1)):
                l = line1[i][0]
                print(line1)
                cv.line(img, (l[0], l[1]), (l[2], l[3]), (0,255,0), 10, cv.LINE_AA)

cv.imshow("img", img)
cv.waitKey(0)
