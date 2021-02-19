# -*- coding: utf-8 -*-
#pip install opencv-python
import cv2

cam = cv2.VideoCapture(0+cv2.CAP_DSHOW)
# cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    vis = img.copy()
    cv2.imshow('Camera', vis)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()