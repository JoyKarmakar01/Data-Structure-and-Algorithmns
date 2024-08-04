"""
Implementing Adjacency Matrix in Python
Let's implement this in Python step-by-step.

Create a class for the graph
Initialize the adjacency matrix
Add edges to the graph
Display the adjacency matrix


"""
class Graph:
    def __init__(self, num_vertices):
        # Initialize a num_vertices x num_vertices matrix with all 0s
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        # Add an edge between vertex u and vertex v
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # For undirected graph

    def display(self):
        for row in self.adj_matrix:
            print(row)

# Example usage
num_vertices = 4  # Number of vertices (A, B, C, D)
graph = Graph(num_vertices)

# Adding edges: A-B, A-C, B-D, C-D
graph.add_edge(0, 1)  # A-B
graph.add_edge(0, 2)  # A-C
graph.add_edge(1, 3)  # B-D
graph.add_edge(2, 3)  # C-D

# Display the adjacency matrix
graph.display()

# num_vertices = 4
# adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
# for row in adj_matrix:
#     print(row) 

# n = 3
# arr = [[0] * n for _ in range(n)]

# print(arr)