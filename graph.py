"""
Module to represent directed/undirected graphs
"""
import copy
from edge import Edge


class Graph(object):
    """
    Graph is represented as a List of Vertex objects
    """
    def __init__(self, vertices, n_v, n_e):
        """
        verices: List of Vertex objects
        n_v: number of vertices in the Graph
        n_e: number of edges in the graph
        """
        self.vertices = vertices
        self.num_of_vertices = n_v
        self.num_of_edges = n_e
        self.repr_str = "G(" + self.num_of_vertices + "," + self.num_of_edges + ")"

    def edges(self):
        """
        Flattens the adjancency list for all vertices and returns the
        edges in the graph
        """
        return [edge for vertex in self.vertices for edge in         vertex.adj]

    def transpose(self):
        """
        Returns the transpose of the graph.
        Time complexity : O(E + V)
        """
        cache = {}
        new_vertices = []
        # Runs O(E) times
        #import ipdb; ipdb.set_trace()
        # create the vertex if its already not
        # created
        for vertex in self.vertices:
            from_val = vertex.val
            from_vertex = cache.get(from_val, None)
            if not from_vertex:
                from_vertex = copy.copy(vertex)
                cache.update({from_val: from_vertex})
            for edge in vertex.adj:
                to_val = edge._to.val
                to_vertex = cache.get(to_val, None)
                if not to_vertex:
                    to_vertex = copy.copy(edge._to)
                    cache.update({to_val: to_vertex})
                # reverse the edge by creating a new edge in
                # reverse direction
                toggled_edge = Edge(to_vertex, from_vertex, edge.directed, edge.weight)
                # add to the ajancency list of the vertex this
                # toggled edge
                to_vertex.adj.append(toggled_edge)
        # Runs O(V) times
        # This is an extra iteration to keep the vertices in the
        # transposed graph in the same order as in the original graph
        for vertex in self.vertices:
            new_vertices.append(cache.get(vertex.val))
        return Graph(new_vertices, self.num_of_vertices, self.num_of_edges)

    def __repr__(self):
        return self.repr_str

    def __str__(self):
        g_string = self.repr_str + "\n"
        for vertex in self.vertices:
            g_string = g_string +  "Vertex: " + str(vertex) + "| Edges: " + str(vertex.adj) + "\n"
        return g_string
