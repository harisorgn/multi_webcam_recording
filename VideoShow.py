from threading import Thread
import cv2

class VideoShow:

    def __init__(self, window_name, frame=None):
        self.frame = frame
        self.window_name = window_name
        self.stopped = False

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
            cv2.imshow(self.window_name, self.frame)
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True