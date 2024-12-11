import cv2
from libs.vision.camera import Camera
from libs.vision.functions import make_object
from libs.vision.classes import Object
from libs.vision.draws import draw_middle_lines, draw_object
from dotenv import load_dotenv
import torch
import time
from AI.classes import Result, Prediction

torch.set_default_device('cuda') # Set the default device to cuda if available
load_dotenv(override=True) # Load the environment variables

camera = Camera()
capture = cv2.VideoCapture(camera.id)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, camera.width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, camera.height)

device = 'cuda' if torch.cuda.is_available() else 'cpu'


def draw_objects(frame, objects: list[Object]) -> None:
    """
    Draw objects on the frame
    """
    for object in objects:
        draw_object(frame, object)


def detect_objects(results:Result) -> list[Object]:
    """
    Detect objects from the results
    """
    boxes = results.predictions
    objects_count = results.objects_count

    if objects_count <= 0:
        return list()

    return [make_object(boxes[i].bbox) for i in range(objects_count)]


def detect(model, robot):
    """ 
    Detect objects in the frame
    """
    prev = 0  # Previous time
    while capture.isOpened():
        time_elapsed = time.time() - prev
        success, frame = capture.read()
        if not success:
            break
        if time_elapsed > 1. / camera.fps:
            result:Result = model.predict(
                frame, conf=0.5, verbose=False, device=device, max_det=5
            )

            

            # if len(results) > 0:
            #     for obj in results:
            #         # Send the class of the object to the robot
            #         robot.send_data("test", obj.boxes.cls.item())
            # else:
            #     # Send -1.0 to the robot if no object is detected
            #     robot.send_data("test", -1.0)

            detects = detect_objects(result)
            draw_objects(frame, detects)
            draw_middle_lines(frame)

            cv2.imshow("Frame", frame)

            prev = time.time()

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    capture.release()
    cv2.destroyAllWindows()
