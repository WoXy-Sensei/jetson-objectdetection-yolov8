import cv2
from libs.vision.camera import Camera
from libs.vision.classes import Object, BBox

camera = Camera()

def draw_middle_lines(frame) -> None:
    """
    Draws the middle lines on the frame
    """
    cv2.line(frame, (0, camera.height // 2),
             (camera.width, camera.height // 2), (0, 255, 0), 2)

    cv2.line(frame, (camera.width // 2, 0),
             (camera.width // 2, camera.height), (0, 255, 0), 2)


def draw_object(frame, object: Object) -> None:
    """
    Draws the object on the frame
    """

    center_x = int(object.center.x)
    center_y = int(object.center.y)
    box: BBox = object.bbox
    x, y, w, h = box.xmin, box.ymin, box.xmax - box.xmin, box.ymax - box.ymin

    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
    cv2.rectangle(frame, (int(x), int(y)),(int(x + w), int(y + h)), (0, 255, 0), 2)
