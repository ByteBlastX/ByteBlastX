class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def count_odd_degree_vertices(self):
        odd_degree_count = 0
        for i in range(self.V):
            if len(self.adj[i]) % 2 != 0:
                odd_degree_count += 1
        return odd_degree_count


# Example usage:
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)
    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    # Count the number of vertices with odd degree
    odd_vertices = g.count_odd_degree_vertices()
    print("Number of vertices with odd degree:", odd_vertices)
