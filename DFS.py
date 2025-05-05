def depth_first_search(graph, start_vertex, visited=None):
    # Initialize visited set if this is the first call
    if visited is None:
        visited = set()
    
    # Mark current vertex as visited
    visited.add(start_vertex)
    
    # Print current vertex (to track the traversal)
    print(start_vertex, end=' ')
    
    # Recursively visit all adjacent vertices that haven't been visited yet
    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)
    
    return visited

# Example usage
if __name__ == "__main__":
    # Represent undirected graph as an adjacency list
    # Each key is a vertex and its value is a list of adjacent vertices
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Depth-First Search starting from vertex 'A':")
    depth_first_search(graph, 'A')