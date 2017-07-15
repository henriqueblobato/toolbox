'''
Created on 14 de jul de 2017

@author: henrique

Input: Video file
Output: JPG image in folder called 'pictures'
Parameters:
    GET_EVERY_N_FRAMES: Save image every n reads on the video
                        Change to 1 if want all the video
'''

import cv2
import os

GET_EVERY_N_FRAMES = 100

cap = cv2.VideoCapture('video.mp4')
frame_count = 1
count2 = 1

if not os.path.exists('frames'):
    os.mkdir('frames')

while(True):
    ret, frame = cap.read()
    if count2 == get_every_n_frames: 
        if not ret: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image_name = 'frames/' + str(frame_count) + '.jpg'
        cv2.imwrite(image_name, gray)
        count2 = 1
    else:
        count2 += 1
    frame_count += 1
        
        
