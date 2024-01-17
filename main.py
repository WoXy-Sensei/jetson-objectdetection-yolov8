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
from draws import draw_middle_lines, draw_object

# enter 0 for webcam, 1 for external camera
capture = cv2.VideoCapture(Camera.id)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, Camera.width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, Camera.height)


cuda = '1'


def draw_objects(frame, objects: list[Object]) -> None:
    """
    Draws the objects on the frame
    """
    for object in objects:
        draw_object(frame, object)


def detect_objects(results) -> list[Object]:
    """
    Detects the objects in the frame
    """

    boxes = results.boxes.xyxy
    objects_count = len(boxes)

    if objects_count <= 0:
        return list()

    return [make_object(boxes[i].tolist()) for i in range(objects_count)]


def main():
    """
    Main function
    """
    model = YOLO('models/best.pt')
    prev = 0

    while capture.isOpened():

        time_elapsed = time.time() - prev
        success, frame = capture.read()
        if success:
            if time_elapsed > 1. / 5:
                prev = time.time()

                results = model.predict(frame, conf=0.5, verbose=False, device='cuda', max_det=5, imgsz=(640, 480))[0]

                detects = detect_objects(results)

                #--------------------------------------------------
                draw_objects(frame, detects)
                draw_middle_lines(frame)
                #--------------------------------------------------

                cv2.imshow("YOLOv8 Inference", frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        else:
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
