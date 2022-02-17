import cv2

#capture = cv2.VideoCapture(0)
image2 = cv2.imread('/home/pi/535_Mechatronics/Mini Project/moja_test_qr.png')
qrCodeDetector = cv2.QRCodeDetector()
decodedText, points, _ = qrCodeDetector.detectAndDecode(image2)

if True:
    #success, img_from_cam = capture.read()
    
    #image = cv2.imread(img_from_cam)
    
    if points is not None:
#         nrOfPoints = len(points)
        
#         for i in range(nrOfPoints):
#             nextPointIndex = (i+1) % nrOfPoints
#             cv2.line(image2, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 3)
        print(decodedText)
        
        cv2.imshow("Image", image2)
        cv2.waitKey(100)
    
 
    else:
        print("QR code not detected")
