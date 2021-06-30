

import cv2
import numpy as np

cap = cv2.VideoCapture("eye.mp4")

while (cap.isOpened()):

    ret, frame = cap.read()

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gray_frame = cv2.GaussianBlur(gray_frame,(7,7),0)

    _, threshold = cv2.threshold(gray_frame,5,255,cv2.THRESH_BINARY_INV)


    contour,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contour = sorted(contour, key=lambda x: cv2.contourArea(x), reverse = True)


    for cnt in contour:

        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x,y), (x+w , y+h), (0,255,0),2)
        cv2.drawContours(frame, [cnt] ,-1, (0,0,255),3)

        v_line = x+int(w/2)
        h_line = y+int(h/2)

        #print(v_line," : Vertical")
        #print(h_line," : Horizontal")

        
        if v_line < 310:
            print("Looking Left")
        elif v_line > 470:
            print("Looking Right")
        else:
            pass

        if h_line < 250:
            print("Looking Up")
        elif h_line > 500 :
            print("Looking Down")
        else:
            pass


        cv2.line(frame,(v_line,0),(v_line,frame.shape[0]),(0,255,255),1)
        cv2.line(frame,(0,h_line),(frame.shape[1],h_line),(0,255,255),1)

        break


    cv2.imshow("threshold",threshold)
    cv2.imshow("frame",frame)


    if cv2.waitKey(50) is ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
