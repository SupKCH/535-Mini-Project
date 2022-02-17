import cv2
import sys

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if data:
        a = data
        print(a)
        break

    cv2.imshow("QRCODEscanner", img)    
    if cv2.waitKey(1) == ord("q"):
        break
    
sys.exit()