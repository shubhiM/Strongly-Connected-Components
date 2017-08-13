"""
Module to compute strongly connected components of the Graph
"""
from graph_generator import GraphGenerator
from dfs import DFS

def write_tree(file_obj, vertex):
    """
    writes the DFS tree for a DFS Forest
    """
    file_obj.write(vertex.val)
    file_obj.write("\n")
    vertex.color = "grey"
    for edge in vertex.adj:
        if edge._to.color != "grey":
            write_tree(file_obj, edge._to)

def write_dfs_components(file_obj, dfs_forest):
    """
    writes the DFS Forest
    """
    for tree in dfs_forest:
        file_obj.write("component")
        file_obj.write("\n")
        write_tree(file_obj, tree)


def strongly_connected_components(filepath):
    """
    Method to calculate the strongly connected
    components in the graph and write it in an output file
    Expects: filepath (filename is sufficient if file is in the same
        directory else absolute file path is required)
    Effects: Generates the output file with name output_filename
    in the same directory
    """
    generator = GraphGenerator(filepath)
    graph = generator.graph_from_text_file()
    dfs_1 = DFS(graph)
    dfs_1.dfs()
    # graph after first run of dfs with vertices ordered by increasing
    # finishing time.
    dfs_1.dfs_graph_from_call_stack()
    # graph after transpose of the original graph
    dfs_1_trans_graph = dfs_1.dfs_graph.transpose()
    # # Second run of dfs on transposed graph
    dfs_2 = DFS(dfs_1_trans_graph)
    dfs_2.dfs()
    dfs_2.dfs_graph_from_call_stack()
    filename = filepath.split("/")[-1]
    file_obj = open("output_" + filename, "w")
    write_dfs_components(file_obj, dfs_2.dfs_forest)
    file_obj.close()
