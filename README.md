# Compute Strongly Connected Components in a Graph

The program starts from the main.py python module which expects a filepath as argument. The
input file needs to be given in the expected format to get the desired output.

## Data structures and classes:
1. A Graph is essentially represented as a list of vertices where lists are the basic python
datatypes. Adjacency list representation of graph is chosen because its both memory efficient
and also DFS essentially is more convenient to implement with such representation.
2. A vertex has a value and an adjacency list along with additional parameters specific to the
DFS search. Adjacency list in a vertex is a list of edges.
3. An edge is represented as a directed edge with a from vertex, to vertex and optional weight
4. Graph generator takes the input file as input and generates the graph object in memory.
5. DFS computes depth first search on graph object

## Algorithm:
```
1. Generates graph from input file - O(E)
2. Computes DFS - O(V + E)
3. Generates a transpose of the original graph which is a new copy of the graph but
transposed. - O(V + E)
4. Computes DFS again on transposed graph - O(V + E)
5. Writes the output to a text file - O(E)
```


## Complexity Analysis:
The overall complexity is O(V + E)

## Sanity Tests:
There are some sample graphs that were used to test the sanity of the code. These can be
found in tests.py

## Efficiency Tests and limitations:
large_graph.py can be used to generate a very large graph with one connected component.
The recursion depth for python is increased as python is very strict about the recursion depths.
The profiling results are as follows for the input size of 2^14. For latter input the program halts
with segmentation fault (out of memory issues). For benchmarking, the program is run on 2.7
GHz Intel Core i5, 8GB DDR3, MacBook Pro.

## How to Run the program:
  1. cd scc
  2. python main.py input_graph.txt
  
## Output:
  1. cd scc
  2. open output_input_graph.txt
