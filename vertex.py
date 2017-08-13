"""
Module define Subclasses of VertexBase class
"""
from vertex_base import VertexBase

class Vertex(VertexBase):
    """
    Represents the Vertex class as required for DFS on G(V, E)
    """
    def __init__(self, **kwargs):
        """
        Expects the following in kwargs
            val: is the string or integer literal representing vertex label
            color: can be anything between [white, grey and black]
            dt: detection time of the vertex, defaults to 0
            ft: finishing time of the vertex, defaults to 0
        """
        super(Vertex, self).__init__(
            kwargs.get('val'), kwargs.get('adj', []))
        self.color = kwargs.get('color', 'white')
        self.detection_time = kwargs.get('dt', 0)
        self.finishing_time = kwargs.get('ft', 0)

    def is_white(self):
        return self.color == "white"

    def is_black(self):
        return self.color == "black"

    def is_grey(self):
        return self.color == "grey"

    def __str__(self):
        return self.val + str((self.detection_time, self.finishing_time)) + " hash:" + str(hash(self))

    def __copy__(self):
        """
        Returns the copy of the vertex without an adjacency list
        """
        return Vertex(**{
            'val': self.val,
            'color': 'white',
            'dt': self.detection_time,
            'ft': self.finishing_time
        })
