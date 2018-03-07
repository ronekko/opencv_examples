from collections.abc import Iterator
import cv2
import matplotlib.pyplot as plt

class VideoReader(Iterator):
    def __init__(self, filepath):
        self.video = cv2.VideoCapture(filepath)

    def __next__(self):
        ret, frame = self.video.read()
        if ret:
            return frame
        else:
            raise StopIteration

    def next(self):
        return self.__next__()

video = VideoReader('bbaf2n.mpg')
for frame in video:
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(frame)
    plt.show()