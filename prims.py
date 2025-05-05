import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (cost, node)
    total_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        total_cost += cost
        print(f"Visited {node}, cost so far: {total_cost}")
        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor))

    return total_cost


# Weighted undirected graph
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('D', 1), ('E', 4)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 1)],
    'E': [('B', 4), ('F', 1)],
    'F': [('C', 5), ('E', 1)]
}

cost = prim(graph, 'A')
print("Total minimum cost:", cost)
