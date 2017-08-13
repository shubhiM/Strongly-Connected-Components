import math

def large_graph(size):
    """
    writes large graph into a file called large graph
    """
    file_obj = open("large_graph.txt", "w")
    #edges = int(math.pow(2, size))
    edges = size
    file_obj.write(str(edges) + " " + str(edges) + "\n")
    for i in range(edges-1):
        file_obj.write(str(i) + " " + str(i+1) + "\n")
    file_obj.write(str(i+1) + " " + str(0) + "\n")
    file_obj.close()
