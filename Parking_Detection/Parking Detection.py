import cv2
import pickle



# img = cv2.resize(img,[1000,1000])
width, height = 107, 48
try:
    with open('CarPosition', 'rb') as f:
        posList = pickle.load(f)
except:
        posList = []

def mouseClick(events,x,y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x< x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarPosition', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (205,0,200), 2)

    # cv2.rectangle(img,(114,77),(150,160),(255,0,255),3)
    cv2.imshow("img",img)
    cv2.setMouseCallback("img", mouseClick)
    cv2.waitKey(1)