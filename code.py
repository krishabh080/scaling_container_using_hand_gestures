import cv2
import  urllib.request
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(maxHands=1 )

cap = cv2.VideoCapture(0)
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector( maxHands = 1)
while True:
    status, photo = cap.read()
    hand = detector.findHands(photo, draw= False)
    if cv2.waitKey(1000) == 13:
        break
    if hand :
        lmlist= hand[0]
        totalFinger=detector.fingersUp(lmlist)
        if totalFinger == [0,1,1,0,0,]:
            print("launching a new container")
            request_url = urllib.request.urlopen("your api url for launching a new container")
            print ( request_url.read() )
        elif totalFinger == [0,1,0,0,0,]:
            print("Removing the container")
            request_url = urllib.request.urlopen("your api url for removing container")
            print ( request_url.read() )
            
        else:
            print("show correct fingers")
cv2.destroyAllWindows()
