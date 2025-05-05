def breadth_first_search(graph, start_vertex):
    # Initialize data structures
    visited = set()
    visited.add(start_vertex)
    
    # Queue to manage the BFS order
    queue = [start_vertex]
    
    # Print starting vertex
    print(start_vertex, end=' ')
    
    # Helper recursive function to implement BFS
    def bfs_recursive(queue):
        # Base case: if queue is empty, we're done
        if not queue:
            return
        
        # Create a new queue for the next level
        next_queue = []
        
        # Process all vertices at the current level
        for vertex in queue:
            # Explore all neighbors of the current vertex
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    # Mark as visited
                    visited.add(neighbor)
                    # Print vertex
                    print(neighbor, end=' ')
                    # Add to next level queue
                    next_queue.append(neighbor)
        
        # Recursive call to process next level
        bfs_recursive(next_queue)
    
    # Start the recursive BFS process
    bfs_recursive(queue)
    
    return visited

# Example usage
if __name__ == "__main__":
    # Represent undirected graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C', 'E']
    }
    
    print("Breadth-First Search starting from vertex 'A':")
    breadth_first_search(graph, 'A')