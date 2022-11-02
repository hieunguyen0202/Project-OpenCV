import cv2
import cvzone
# Sum points in face
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    imgText = np.zeros_like(img)
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        #W small
        #draw eye
        # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        # cv2.circle(img, pointLeft,5,(255,0,255), cv2.FILLED)
        # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w,_ = detector.findDistance(pointLeft,pointRight)
        # male 6.3 cm
        W = 6.3
        # d = 50
        # #finding the Focal length
        # f = (w*d)/W
        # print(f)

        # Finding distance
        f = 642
        d = (W*f)/w
        print(d)
        cvzone.putTextRect(img, f'Depth: {int(d)}cm',
                           (face[10][0]-75, face[10][1]-70), scale = 2)

    imgStacked = cvzone.stackImages([img,imgText], 2, 1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)