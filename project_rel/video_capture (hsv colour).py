# -*- coding: utf-8 -*-

#Created on Mon Dec  7 13:10:02 2020

#@author: kaifr

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    _, frame = cap.read()
    hsv_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # white colour
    low=np.array([0,42,0])
    high=np.array([179,255,255])
    mask=cv2.inRange(hsv_frame ,low , high)
    result= cv2.bitwise_and(frame , frame, mask=mask)
    
    #blue colour
    low_blue=np.array([94,80,2])
    high_blue=np.array([126,255,255])
    blue_mask=cv2.inRange(hsv_frame , low_blue,high_blue)
    mask_b=cv2.bitwise_and(frame , frame, mask=blue_mask)
    cv2.imshow('frame', frame)
    cv2.imshow("blue",blue_mask)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()