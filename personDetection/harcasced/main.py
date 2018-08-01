import cv2
import time
import os
import time

person_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
cap = cv2.VideoCapture("../video2.mp4")
#fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
#print "the actual fps is {}".format(fps)
#frame_number = 120
#start = time.time()
while True:
#for i in xrange(frame_number):    
    r, frame = cap.read()
    if r:
        start_time = time.time()
        frame = cv2.resize(frame,(640,360)) # Downscale to improve frame rate
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # Haar-cascade classifier needs a grayscale image
        rects = person_cascade.detectMultiScale(gray_frame)  #tect stores the coorinate of person detected and  the width and hight of that box
        
        end_time = time.time()
        print("Elapsed Time:",end_time-start_time)
            
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
        cv2.imshow("preview", frame)
    k = cv2.waitKey(1)

    if k & 0xFF == ord("q"): # Exit condition
        break
#end = time.time()
#print (frame_number/(end-start))