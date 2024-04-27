def max_edges_in_complete_graph(n):
    # Calculate the maximum number of edges using the formula n(n-1)/2
    max_edges = (n * (n - 1)) // 2
    return max_edges

if __name__ == "__main__":
    # Take input for the number of vertices in the complete graph
    num_vertices = int(input("Enter the number of vertices in the complete graph (n): "))
    
    # Calculate the maximum number of edges
    max_edges = max_edges_in_complete_graph(num_vertices)
    print("Maximum number of edges in the complete graph:", max_edges)
