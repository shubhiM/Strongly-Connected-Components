"""
Module to define base classes for Graph Edges
"""
import copy

class EdgeBase(object):
    """
    Represents the most general edge in a Graph
    """
    def __init__(self, _from, _to, directed=True, weight=None):
        """
        _to: represents vertex at one end of the edge
        _from: represents vertex at the other end of the edge
        directed: if true then direction is enforced on the edge
        weight: any integer value.
        """
        self._from = _from
        self._to = _to
        self.directed = directed
        self.weight = weight

    def toggle(self):
        """
        Returns a new edge with reversed direction
        """
        return EdgeBase(
            copy.deepcopy(self._to), copy.deepcopy(self._from), self.directed, self.weight)

    def __str__(self):
        #TODO: why do we require explicit typecasting to str
        # when there is already an str function defined for
        # Vertex class
        return str(self._from) +  '-->' + str(self._to)

    def __repr__(self):
        return str(self._from) +  '-->' + str(self._to)
