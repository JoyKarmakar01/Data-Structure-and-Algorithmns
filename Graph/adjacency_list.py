# Define the Graph class using an adjacency list
class Graph:
    def __init__(self, num_vertices):
        # Initialize the number of vertices
        self.num_vertices = num_vertices
        # Initialize the adjacency list, which is a list of empty lists
        self.adj_list = [[] for _ in range(num_vertices)]

    # Method to add an edge from vertex u to vertex v
    def add_edge(self, u, v):
        # Add vertex v to the adjacency list of vertex u
        self.adj_list[u].append(v)
        # Add vertex u to the adjacency list of vertex v (since it's an undirected graph)
        self.adj_list[v].append(u)

    # Method to print the adjacency list
    def print_graph(self):
        # Iterate through each vertex
        for i in range(self.num_vertices):
            # Print the current vertex number
            print(f"Vertex {i}: ", end="")
            # Iterate through each neighbor of the current vertex
            for neighbor in self.adj_list[i]:
                # Print the neighbor vertex
                print(f"{neighbor} ", end="")
            # Print a newline for the next vertex
            print()

# Example usage of the Graph class
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)

    # Add some edges between the vertices
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    # Print the adjacency list of the graph
    g.print_graph()
