"""
Module defines test functions.
"""
from graph_generator import GraphGenerator
from dfs import DFS


def foo(vertex):
    print vertex.val
    vertex.color = "grey"
    for edge in vertex.adj:
        if edge._to.color != "grey":
            foo(edge._to)

def print_dfs_components(dfs_forest):
    for tree in dfs_forest:
        print "component"
        foo(tree)

def object_references(graph):
    """
    checks if all the vertices in a graph are essentially the same
    object references
    """
    vertex_hash = {vertex.val: hash(vertex) for vertex in graph.vertices}
    error = False
    for vertex in graph.vertices:
        for edge in vertex.adj:
            error = True if (vertex_hash.get(edge._to.val) != hash(edge._to)) and (vertex_hash.get(edge._from.val) != hash(edge._from)) else False
            if error:
                return "failed at" + str(edge)
    return "object references test passed"

def run_tests():
    """
    runs all the tests for the program
    """
    generator = GraphGenerator('graph.txt')
    graph = generator.graph_from_text_file()
    # test for object references in original graph

    print "TEST: Testing object reference on original graph"
    print object_references(graph)

    dfs_1 = DFS(graph)
    dfs_1.dfs()

    # graph after first run of dfs with vertices ordered by increasing
    # finishing time.
    dfs_1.dfs_graph_from_call_stack()

    # test for object reference after first dfs run
    print "TEST: Testing object reference on dfs 1 graph"
    print object_references(dfs_1.dfs_graph)

    print "Printing DFS 1 Graph"
    print dfs_1.dfs_graph

    print "*****************************************"
    # graph after transpose of the original graph
    dfs_1_trans_graph = dfs_1.dfs_graph.transpose()

    print "Printing transpose of DFS 1 Graph"
    print dfs_1_trans_graph

    print "*****************************************"

    # # Second run of dfs on transposed graph
    dfs_2 = DFS(dfs_1_trans_graph)
    dfs_2.dfs()
    dfs_2.dfs_graph_from_call_stack()
    # test for object reference after first dfs run

    print "TEST: Testing object reference on dfs 2 graph"
    print object_references(dfs_2.dfs_graph)

    print "Printing DFS 2 Graph"
    print dfs_2.dfs_graph

    print "*****************************************"

    print "Printing DFS components"

    print "*****************************************"
    print_dfs_components(dfs_2.dfs_forest)
