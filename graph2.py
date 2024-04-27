class CompleteGraph:
    def __init__(self, n):
        self.n = n

    def max_degree_per_vertex(self):
        # Maximum degree of each vertex in a complete graph with n vertices is n-1
        return self.n - 1

if __name__ == "__main__":
    # Take input for the number of vertices in the complete graph
    num_vertices = int(input("Enter the number of vertices in the complete graph (n): "))
    
    # Create a complete graph with the given number of vertices
    complete_graph = CompleteGraph(num_vertices)

    # Find the maximum degree of each vertex
    max_degree = complete_graph.max_degree_per_vertex()
    print("Maximum degree of each vertex in the complete graph:", max_degree)
