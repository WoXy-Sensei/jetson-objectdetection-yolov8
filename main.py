import math
import time
from ultralytics import YOLO
import cv2
from vision.camera import Camera
from vision.functions import make_object
from vision.classes import Object
from vision.draws import draw_middle_lines, draw_object
from dotenv import load_dotenv
import numpy as np
import torch
from robot import Robot


torch.set_default_device('cuda')
load_dotenv()

# enter 0 for webcam, 1 for external camera
capture = cv2.VideoCapture(Camera.id)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, Camera.width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, Camera.height)

device = 'cuda'

model_path = 'models/best.pt'  # enter the path to the model


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


def detect():
    """
    Main function
    """
    model = YOLO(model_path)

    prev = 0

    robot = Robot()

    while capture.isOpened():

        time_elapsed = time.time() - prev
        success, frame = capture.read()
        if success:
            if time_elapsed > 1. / Camera.fps:

                results = model.predict(frame, conf=0.5, verbose=False, device=device , max_det=5, imgsz=(640, 480))[0]
                for obj in results:
                    print(obj.boxes.cls.item())
                    robot.send_data("test", obj.boxes.cls.item())

                detects = detect_objects(results)

                # --------------------------------------------------
                draw_objects(frame, detects)
                draw_middle_lines(frame)
                # --------------------------------------------------
       
             
                cv2.imshow("YOLOv8 Inference", frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        else:
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect()
