"""
FRC: 2024 Game Element Custom Decision

Author: Bardia Ramez - 2024
"""

import math
import sys
import time
import numpy as np
from ultralytics import YOLO
import os
import cv2
from camera import Camera
from functions import make_object
from classes import BBox, Object
from time import sleep

# enter 0 for webcam, 1 for external camera
capture = cv2.VideoCapture(Camera.id)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, Camera.width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, Camera.height)


cuda = '1'  # set to False if using CPU


def detect_objects(boxes) -> list[Object]:
    objects = []
    object_count = len(boxes)
    if object_count > 0:
        for i in range(object_count):
            box = boxes[i].tolist()
            # print(f" OBJEEE {i}",box)
            b = BBox(
                xmin=box[0],
                ymin=box[1],
                xmax=box[2],
                ymax=box[3])

            objects.append(make_object(b))

    return objects


def main():
    # Load the YOLOv8 model
    model = YOLO('models/best.pt')
    prev = 0

    # Loop through the video frames
    while capture.isOpened():
        # Read a frame from the video

        time_elapsed = time.time() - prev
        success, frame = capture.read()
        if success:
            if time_elapsed > 1. / 5:
                prev = time.time()

                results = model.predict(
                    frame, conf=0.5, verbose=False, device='cuda', max_det=5, imgsz=(640, 480))[0]

                annotated_frame = results.plot()
                boxes = results.boxes.xyxy
                detected = detect_objects(boxes)
                if len(detected) > 0:
                    x = int(detected[0].center.x)
                    y = int(detected[0].center.y)
                    cv2.circle(annotated_frame, (x, y), 5, (0, 0, 255), -1)

                    print(detected[0].angles.tx, detected[0].angles.ty)

                cv2.line(annotated_frame, (0, Camera.height // 2),
                         (Camera.width, Camera.height // 2), (0, 255, 0), 2)

                cv2.line(annotated_frame, (Camera.width // 2, 0),
                         (Camera.width // 2, Camera.height), (0, 255, 0), 2)

                cv2.imshow("YOLOv8 Inference", annotated_frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        else:
            break

    capture.release()
    cv2.destroyAllWindows()


main()
