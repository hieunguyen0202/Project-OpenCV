import cv2
import cvzone
# Sum points in face
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
textList = ["Welcome to My project. ",
            "Here we will study"," Computer Vision and AI","Closer","Faraway"]
sen = 10 #more is less
while True:
    success, img = cap.read()
    imgText = np.zeros_like(img)
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        w,_ = detector.findDistance(pointLeft,pointRight)
        # male 6.3 cm
        W = 6.3

        f = 642
        d = (W*f)/w
        print(d)
        cvzone.putTextRect(img, f'Depth: {int(d)}cm',
                           (face[10][0]-75, face[10][1]-70), scale = 2)

        for i, text in enumerate(textList):
            singleHeight = 50 + int((int(d/sen)*sen)/4)
            scale = 0.4 + (int(d/sen)*sen)/70
            cv2.putText(imgText,text,(50,50+(i*singleHeight)),
                        cv2.FONT_ITALIC, scale,(255,255,255),2)
    imgStacked = cvzone.stackImages([img,imgText], 2, 1)
    cv2.imshow("Image", imgStacked)
    cv2.waitKey(1)