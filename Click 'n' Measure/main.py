import cv2 
import numpy as np
import os
import utils

webcam = False
script_dir = os.path.dirname(__file__)
image_filename = '2.jpg'
path = os.path.join(script_dir, image_filename)

cap = cv2.VideoCapture(0)
cap.set(10, 160)  # brightness
cap.set(3, 1920)  # width
cap.set(4, 1018)  # height
scale = 3
wP = 210 * scale
hP = 297 * scale

while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread(path)

    imgContours, conts = utils.getContours(img, minArea=50000, filter=4)

    if len(conts) != 0:
        biggest = conts[0][2]
        imgWarp = utils.warpImg(img, biggest, wP, hP)

        imgContours2, conts2 = utils.getContours(imgWarp, minArea=2000, filter=4, cThr=[50, 50], draw=False)

        if len(conts2) != 0:
            for obj in conts2:
                cv2.polylines(imgContours2, [obj[2]], True, (0, 255, 0), 2)
                nPoints = utils.reorder(obj[2])
                nW = round(utils.findDis(nPoints[0][0] // scale, nPoints[1][0] // scale) / 10, 1)
                nH = round(utils.findDis(nPoints[0][0] // scale, nPoints[2][0] // scale) / 10, 1)

                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]), (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]), (255, 0, 255), 3, 8, 0, 0.05)

                x, y, w, h = obj[3]

                cv2.putText(imgContours2, '{}cm'.format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
                cv2.putText(imgContours2, '{}cm'.format(nH), (x - 30, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

        cv2.imshow('A4', imgContours2)

    img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    cv2.imshow('Original', img)

    cv2.waitKey(1) 
        


