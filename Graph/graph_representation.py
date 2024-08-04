
"""
This is Graph Representation for Adjoint Matrix..

"""

"""
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0]* num_vertices for _ in range(num_vertices)]

    def add_edge(self,u,v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def display(self):
        for row in self.adj_matrix:
            print(row)


num_vertices = 4
graph = Graph(num_vertices)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,3)
graph.add_edge(2,3)

graph.display()
"""

"""This is Adjacency List for Graph Representation.."""

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for i in range(self.num_vertices):
            print(f"Vertex {i}: ", end="")
            for neighbor in self.adj_list[i]:
                print(f"{neighbor} ", end="")
            print()

if __name__ == "__main__":
    num_vertices = 5
    graph = Graph(num_vertices)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print_graph()