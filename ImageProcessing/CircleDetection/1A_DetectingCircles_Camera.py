#Program with the best Parameters

import cv2
import numpy as np

img = cv2.imread('camera-lens.jpg',0)
bimg = cv2.medianBlur(img,1)
cimg = cv2.cvtColor(bimg,cv2.COLOR_GRAY2BGR)




circles = cv2.HoughCircles(bimg,cv2.HOUGH_GRADIENT,1,1,
                            param1=25,param2=160,minRadius=0,maxRadius=0)

count = 0
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),2)
        count = count + 1
print('Circles = {}'.format(count))
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()