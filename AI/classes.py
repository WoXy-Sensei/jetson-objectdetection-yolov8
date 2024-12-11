import collections


class Result(collections.namedtuple('Result', [
    'objects_count',
    'predictions',
])):

    """ 
    A class to represent the result of a prediction
    """

    __slots__ = ()

class Prediction(collections.namedtuple('Prediction', [
    'cls',
    'bbox',
])):

    """ 
    A class to represent a prediction
    """

    __slots__ = ()