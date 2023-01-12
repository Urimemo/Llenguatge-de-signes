import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import math
import numpy as np

cap = cv2.VideoCapture(0)   
detector = HandDetector(maxHands=1)
classifier = Classifier("model/keras_model.h5", "model/labels.txt")

offset = 20
imgSize = 300
counter = 0

labels = ["A"]

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  
    rect = cv2.rectangle(img, (25,25), (610,460), (100,255,80), 5)

    #image = cv2.rectangle(image, start_point, end_point, color, thickness)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3),np.uint8)*255
        imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h/w
 
        if aspectRatio > 1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            try: 
                imgResize = cv2.resize(imgCrop,(wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize-wCal)/2)
                imgWhite[:, wGap:wCal+wGap] = imgResize
            except:
                print("ERROR_1")
            prediction, index = classifier.getPrediction(imgWhite)
            print(prediction, index)

        else:
            k = imgSize/w
            hCal = math.ceil(k*h )
            try:
                imgResize = cv2.resize(imgCrop,(imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize-hCal)/2)
                imgWhite[hGap:hCal+hGap, :] = imgResize
            except:
                print("ERROR_2")
            prediction, index = classifier.getPrediction(imgWhite)
            print(prediction, index)

        #cv2.imshow("Cropped image", imgCrop)
        cv2.imshow("white image", imgWhite)

    cv2.imshow("IMG", img)

    esc = cv2.waitKey(1) 
    if esc ==27:
        break