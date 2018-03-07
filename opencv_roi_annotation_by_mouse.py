# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:58:41 2018

@author: ryuhei
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

import chainer
import chainer.functions as F
import chainer.links as L
from chainer import cuda, Variable


if __name__ == '__main__':
    x = np.random.rand(640, 480, 3)
    print('''You can select multiple rectangle regions by "dragging mouse and
pressing Enter key" until you pressed Esc key.''')
    r = cv2.selectROIs('annotation', x)
    cv2.destroyAllWindows()
    print(r)