from graph import Graph
import sys
sys.setrecursionlimit(30000)

class DFS(object):
    def __init__(self, graph):
        """
        Expects graph object as input
        """
        self.graph = graph
        self.time = 0
        self.call_stack = []
        self.dfs_graph = None
        # dfs forest is a list of vertices where each vertex
        # representing root of a DFS forest
        self.dfs_forest = []

    def dfs(self):
        """
        Outer Loop DFS
        """
        while self.graph.vertices:
            # we are doing this so we can generalize the
            # dfs call for the second run
            # it also helps in freeing up the
            # memory utilized by the graph
            vertex = self.graph.vertices.pop()
            if vertex.is_white():
                self.dfs_forest.append(vertex)
                self.dfs_visit(vertex)

    def dfs_visit(self, vertex):
        """
        Inner loop DFS
        """
        self.time = self.time + 1
        vertex.color = "grey"
        vertex.detection_time = self.time
        for edge in vertex.adj:
            if edge._to.is_white():
                self.dfs_visit(edge._to)
        self.time = self.time + 1
        vertex.finishing_time = self.time
        vertex.color = "black"
        # preserving the call stack helps
        # to organize the list of vertices in
        # the graph by their finishing times
        self.call_stack.append(vertex)

    def dfs_graph_from_call_stack(self):
        """
        Generates a new graph in which vertices are all
        ordered by their call stack
        """
        self.dfs_graph = Graph(self.call_stack, self.graph.num_of_vertices, self.graph.num_of_edges)
