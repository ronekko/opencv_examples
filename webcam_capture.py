# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:26:09 2017

@author: sakurai
"""

import cv2


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    # Press 'q' key to stop capture.
    while cv2.waitKey(1) == ord('q'):
        ret, image = cap.read()
        cv2.imshow('camera', image)

    cap.release()
    cv2.destroyAllWindows()
