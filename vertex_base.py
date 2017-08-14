"""
Module to define base classes for Graph Vertex
"""

class VertexBase(object):
    """
    Represents the most general Vertex in Graph
    """
    def __init__(self, val, adj=[]):
        """
        A vertex in a graph has a value and an adjancency list
            val: any string/integer literal.
            adj: List of Edges that this vertex is connected to
        """
        self.val = val
        self.adj = adj

    def __repr__(self):
        return self.val

    def __str__(self):
        return self.val
