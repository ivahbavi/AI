def is_valid_coloring(graph, colors):
    """
    Check if the current coloring is valid

    Args:
        graph: Dictionary representing the graph, where keys are vertices and values are lists of adjacent vertices
        colors: Dictionary mapping vertices to their assigned colors
    
    Returns:
        Boolean: True if coloring is valid, False otherwise
    """
    for vertex in graph:
        if vertex in colors:
            for neighbor in graph[vertex]:
                if neighbor in colors and colors[neighbor] == colors[vertex]:
                    return False
    return True

def color_graph(graph, available_colors, vertex_order=None):
    """
    Color the graph using backtracking
    
    Args:
        graph: Dictionary representing the graph, where keys are vertices and values are lists of adjacent vertices
        available_colors: List of colors that can be used
        vertex_order: Optional list specifying the order in which to color vertices
    
    Returns:
        Dictionary mapping vertices to colors, or None if no solution exists
    """
    if vertex_order is None:
        # Default to ordering by degree (most constrained first)
        vertex_order = sorted(graph.keys(), key=lambda v: len(graph[v]), reverse=True)
    
    def backtrack(colors, index):
        # Base case: all vertices colored
        if index == len(vertex_order):
            return colors
        
        current_vertex = vertex_order[index]
        
        # Try each color for the current vertex
        for color in available_colors:
            colors[current_vertex] = color
            
            # Check if this coloring is valid
            if is_valid_coloring(graph, colors):
                # Recursively color the rest of the graph
                result = backtrack(colors, index + 1)
                if result is not None:
                    return result
            
            # Backtrack by removing the color assignment
            colors.pop(current_vertex)
        
        return None
    
    return backtrack({}, 0)

# Example usage
if __name__ == "__main__":
    # Example graph representation (adjacency list)
    # Each vertex is connected to the vertices in its list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    
    available_colors = ['Red', 'Green', 'Blue']
    
    # Solve the graph coloring problem
    solution = color_graph(graph, available_colors)
    
    if solution:
        print("Graph coloring solution found:")
        for vertex, color in solution.items():
            print(f"Vertex {vertex}: {color}")
    else:
        print("No solution exists with the given colors.")
    
    # Example with a different number of colors
    available_colors = ['Red', 'Green']
    solution = color_graph(graph, available_colors)
    
    if solution:
        print("\nGraph coloring solution with 2 colors:")
        for vertex, color in solution.items():
            print(f"Vertex {vertex}: {color}")
    else:
        print("\nNo solution exists with only 2 colors.")