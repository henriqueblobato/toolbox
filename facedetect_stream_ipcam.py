'''
Created on 15 de jul de 2017

@author: henrique

Detecção de um rosto por meio de um stream de uma câmera IP
Face detect for a ip camera stream

'''
import cv2
import time

faceCascade = cv2.CascadeClassifier('<whole path>/haarcascade_frontalface_alt.xml')

video_capture = cv2.VideoCapture('http://<url to camera stream>')

count = 0
while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        file_name = 'faces_detected/frame%s_%s.png' %(count, str(time.time())[11:])
        cv2.imwrite(file_name, frame)
        count += 1

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
