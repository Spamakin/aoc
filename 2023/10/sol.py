import networkx as nx
from itertools import product

def main():
    path = "input.txt"

    lines = []
    with open(path, "r") as f:
        for line in f:
           lines.append(line.strip())

    G = nx.Graph()
    n = len(lines)
    m = len(lines[0])
    for i in range(n):
        for j in range(m):
            G.add_node((i, j))

    start = (None, None)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "|":
                if i - 1 >= 0:
                    G.add_edge((i, j), (i - 1, j))
                if i + 1 < n:
                    G.add_edge((i, j), (i + 1, j))
            if c == "-":
                if j - 1 >= 0:
                    G.add_edge((i, j), (i, j - 1))
                if j + 1 < m:
                    G.add_edge((i, j), (i, j + 1))
            if c == "L":
                if i - 1 >= 0:
                    G.add_edge((i, j), (i - 1, j))
                if j + 1 < m:
                    G.add_edge((i, j), (i, j + 1))
            if c == "J":
                if i - 1 >= 0:
                    G.add_edge((i, j), (i - 1, j))
                if j - 1 >= 0:
                    G.add_edge((i, j), (i, j - 1))
            if c == "7":
                if i + 1 < n:
                    G.add_edge((i, j), (i + 1, j))
                if j - 1 >= 0:
                    G.add_edge((i, j), (i, j - 1))
            if c == "F":
                if i + 1 < n:
                    G.add_edge((i, j), (i + 1, j))
                if j + 1 < m:
                    G.add_edge((i, j), (i, j + 1))
            if c == "S" and start == (None, None):
                start = (i, j)
        i += 1

    # Get some neighbor of start
    neighbors = []
    for (i, j) in product(range(n), range(m)):
        if G.has_edge((i, j), start):
            neighbors.append((i, j))
    neighbor = neighbors[0]
    # Delete edge
    G.remove_edge(neighbor, start)
    # Find distance from neighbor to start
    distance = nx.shortest_path_length(G, source=neighbor, target=start)
    # Repairs
    distance += 1
    distance //= 2
    G.add_edge(neighbor, start)
    print(f"{distance = }")

if __name__ == "__main__":
    main()
