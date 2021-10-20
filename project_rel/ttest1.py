import cv2

cap= cv2.videocapture(0)

while True:
    _,frame = cap.read()
    
    cv2.imshow("Frame",frame)
    
    key= cv2.waitkey(1)
    if key == 27:
        break
