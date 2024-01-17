import collections

Object = collections.namedtuple('Object', ['bbox', 'area', 'center', 'angles', 'distance'])


class BBox(collections.namedtuple('BBox', ['xmin', 'ymin', 'xmax', 'ymax'])):
    """
    Bounding box
    Represents a rectangle which sides are either vertical or horizontal, parallel
    to the x or y axis
    """
    __slots__ = ()


class Angles(collections.namedtuple('Angles', ['tx', 'ty'])):
    """
    Angles
    Represents an ordered pair that points to the absolute angle of the target
    """
    __slots__ = ()


class Point(collections.namedtuple('Angles', ['x', 'y'])):
    """
    Point
    Represents an ordered pair
    """
    __slots__ = ()


