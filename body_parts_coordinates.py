import cv2
import mediapipe as mp 
import pandas as pd
import numpy as np
import tensorflow as tf 
import os
mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose

cap=cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.7,min_tracking_confidence=0.7) as pose:
    while cap.isOpened():
        ret,frame=cap.read()
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)   
        frame.flags.writeable= False
        result=pose.process(image)
        frame.flags.writeable=True
        image=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(image,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)

        cv2.imshow("cam",image)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()




