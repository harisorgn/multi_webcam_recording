from threading import Thread
import argparse
import cv2
from CountsPerSec import CountsPerSec
from VideoGet import VideoGet

def putIterationsPerSec(frame, iterations_per_sec):

    cv2.putText(frame, "{:.0f} iterations/sec".format(iterations_per_sec),
        (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
    return frame


n_cameras = 2

video_get_v = []
window_title_v = []

for i in range(0, n_cameras):

    window_title_v.append(f"camera {i}")
    cv2.namedWindow(window_title_v[i])

    video_get_v.append(VideoGet(i))
    video_get_v[i].start()

#cv2.namedWindow("cam 1")
#cv2.namedWindow("cam 2")

#video_getter_1 = VideoGet(0).start()
#video_getter_2 = VideoGet(1).start()

cps = CountsPerSec().start()

while True:

    if (cv2.waitKey(1) == ord("q")):
        for i in range(0, n_cameras):
            video_get_v[i].stop()
        break

    for i in range(0, n_cameras):
        frame = video_get_v[i].frame
        frame = putIterationsPerSec(frame, cps.countsPerSec())

        cv2.imshow(window_title_v[i], frame)

    cps.increment()