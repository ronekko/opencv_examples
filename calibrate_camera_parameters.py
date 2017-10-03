# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:20:02 2017

@author: sakurai
"""

import cv2
import numpy as np


def grid_points(n_rows, n_cols):
    points = np.zeros((n_rows * n_cols, 3), np.float32)
    points[:, :2] = np.mgrid[:n_cols, :n_rows].T.reshape(-1, 2)
    return points


if __name__ == '__main__':
    n_rows, n_cols = 10, 7

    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    points_image = []
    counts = 0
    cap = cv2.VideoCapture(0)
    while cv2.waitKey(100) == 255:  # Press any key to stop capture.
        ret, image = cap.read()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (n_cols, n_rows), None)

        if ret:
            corners2 = cv2.cornerSubPix(
                gray, corners, (11, 11), (-1, -1), criteria)
            points_image.append(corners2)

            image = cv2.drawChessboardCorners(image, (n_cols, n_rows),
                                              corners2, ret)
            counts += 1
            print('#', counts)
        else:
            image[:10, :, 2] = 255
            image[-10:, :, 2] = 255
            image[:, :10, 2] = 255
            image[:, -10:, 2] = 255
        cv2.imshow('image', image)
    cap.release()
    cv2.destroyAllWindows()

    points = grid_points(n_rows, n_cols)
    points_board = [points] * len(points_image)
    ret, camera_matrix, distortion_coef, rvecs, tvecs = cv2.calibrateCamera(
        points_board, points_image, gray.shape[::-1], None, None)
    np.savetxt('camera_matrix.txt', camera_matrix,
               header='Camera intrinsic parameter matrix')
    np.savetxt('distortion_coef.txt', distortion_coef,
               header='Camera distortion coefficients')
