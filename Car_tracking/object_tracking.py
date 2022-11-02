import cv2
from tracker import *
import math

trackers = EuclideanDistTracker()
cap = cv2.VideoCapture("test1.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold = 40)

while True:
    _, frame = cap.read()
    roi = frame[140:720, 300: 800]
    #object detection

    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 250, 255, cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 150:
            # cv2.drawContours(frame, [cnt],-1,(0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])

    #tracking
    boxes_ids = trackers.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0 ,0),2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("roi", roi)
    cv2.imshow("Video", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
