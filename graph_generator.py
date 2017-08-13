"""
Module to handle creation of graph object in memory from
external data sources
"""
from vertex import Vertex
from edge import Edge
from graph import Graph


class GraphGenerator(object):
    """
    Define methods to create graph objects
    """

    def __init__(self, filepath):
        """
        Expects the path to be absolute
        """
        self.filepath = filepath

    def graph_from_text_file(self):
        """
        Returns a Graph object from a given text file
        """
        cache = {}
        input_file = open(self.filepath)
        num_of_vertices, num_of_edges = input_file.readline().split(" ")
        num_of_edges = num_of_edges.strip("\n")
        for line in input_file:
            _from, _to = line.split(' ')
            _to = _to.strip("\n")
            _from_vertex = cache.get(_from, None)
            _to_vertex = cache.get(_to, None)
            # creates new vertex in graph if it is not in cache
            if not _from_vertex:
                _from_vertex = Vertex(**{'val': _from})
                cache.update({
                    _from: _from_vertex})
            if not _to_vertex:
                _to_vertex = Vertex(**{'val': _to})
                cache.update({_to: _to_vertex})
            _from_vertex.adj.append(Edge(_from_vertex, _to_vertex))
        input_file.close()
        graph_vertices = cache.values()
        return Graph(graph_vertices, num_of_vertices, num_of_edges)
