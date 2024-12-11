from libs.vision.classes import BBox, Point, Angles, Object
from libs.vision.camera import Camera
import numpy as np
import math


camera = Camera()

def get_area(b: BBox) -> float:
    """Returns the area of a bounding box"""
    return (b.xmax - b.xmin) * (b.ymax - b.ymin)


def get_center(b: BBox) -> Point:
    """Returns the coordinates of the center of a bounding box"""
    return Point(
        (float(b.xmin) + float(b.xmax)) / 2,
        (float(b.ymin) + float(b.ymax)) / 2
    )


def get_angles(b: BBox) -> Angles:
    """Returns x and y angles (in degrees) of the center of a bounding box"""
    p = get_center(b)

    px = p.x
    py = p.y

    # normalizing coordinates
    nx = (1/(camera.width/2)) * (px - ((camera.width / 2) - 0.5))
    # normalizing coordinates
    ny = (1/(camera.height/2)) * (((camera.height / 2) - 0.5) - py)

    vpw = 2.0 * np.tan(camera.horizontal_FOV / 2)  # visual plane width
    vph = 2.0 * np.tan(camera.vertical_FOV / 2)  # visual plane height

    x = vpw / 2 * nx
    y = vph / 2 * ny

    ax = np.arctan(x) * 180 / math.pi
    ay = np.arctan(y) * 180 / math.pi

    return Angles(float(ax), float(ay))  # degrees


def make_object(box) -> Object:
    box: BBox = BBox(
        xmin=box[0],
        ymin=box[1],
        xmax=box[2],
        ymax=box[3])

    """Returns an Object"""
    return Object(
        bbox=box,
        area=get_area(box),
        center=get_center(box),
        angles=get_angles(box),
        distance=0.0
    )
