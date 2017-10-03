# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:08:09 2017

@author: sakurai

See https://github.com/opencv/opencv_contrib/blob/3.3.0/modules/aruco/tutorials/aruco_detection/aruco_detection.markdown
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np



if __name__ == '__main__':
    marker_id = 23
    marker_size = 200
    camera_matrix_path = 'camera_matrix.txt'
    distortion_coef_path = 'distortion_coef.txt'

    # Load camera parameters
    camera_matrix = np.loadtxt(camera_matrix_path)
    distortion_coef = np.loadtxt(distortion_coef_path)

    # Generate a marker image
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    marker_image = cv2.aruco.drawMarker(dictionary, marker_id, 100)
    plt.matshow(marker_image, cmap=plt.cm.gray)
    plt.show()
    cv2.imwrite('marker{}.jpg'.format(marker_id), marker_image)

    cap = cv2.VideoCapture(0)
    while cv2.waitKey(1) == 255:  # To stop capturing, press any key
        ret, image = cap.read()

        # Detect the marker and estimate its location and pose
        corners, ids, rejected = cv2.aruco.detectMarkers(image, dictionary)
        rvecs, tvecs = cv2.aruco.estimatePoseSingleMarkers(
            corners, marker_size, camera_matrix, distortion_coef)

        # Draw detected marker and its location and pose
        cv2.aruco.drawDetectedMarkers(image, corners, ids)
        if rvecs is not None and tvecs is not None:
            for rvec, tvec in zip(rvecs, tvecs):
                cv2.aruco.drawAxis(
                    image, camera_matrix, distortion_coef, rvec, tvec, 100)

        cv2.imshow('camera', image)

    cv2.destroyAllWindows()
    cap.release()
