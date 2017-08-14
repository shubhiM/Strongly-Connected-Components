"""
Entry point to execute code for strongly connected components
"""
import sys
from scc import strongly_connected_components

if __name__ == "__main__":
    if len(sys.argv) > 1:
        strongly_connected_components(sys.argv[1])
    else:
        sys.exit("usage:  python main.py <input_file_path>")
