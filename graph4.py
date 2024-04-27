class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_matrix = [[0] * n for _ in range(n)]
    
    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
    
    def is_connected(self):
        # Perform Depth-First Search (DFS) to check if the graph is connected
        visited = [False] * self.n
        self.dfs(0, visited)
        # If any vertex is not visited after DFS, the graph is not connected
        if False in visited:
            return False
        return True

    def dfs(self, v, visited):
        visited[v] = True
        for u in range(self.n):
            if self.adj_matrix[v][u] == 1 and not visited[u]:
                self.dfs(u, visited)


if __name__ == "__main__":
    # Take input for the number of vertices in the graph
    num_vertices = int(input("Enter the number of vertices in the graph (n): "))
    
    # Create a graph with the given number of vertices
    graph = Graph(num_vertices)

    # Take input for the number of edges in the graph
    num_edges = int(input("Enter the number of edges in the graph: "))
    print("Enter the edges (vertex pairs):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    # Check if the graph is connected
    if graph.is_connected():
        print("The graph is connected.")
    else:
        print("The graph is not connected.")
