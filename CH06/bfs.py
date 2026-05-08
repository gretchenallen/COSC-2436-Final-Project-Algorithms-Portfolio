"""
Lab 6: Breadth-First Search Implementation
Finds shortest path (by number of edges) in unweighted graph.
"""
from typing import List, Dict, Optional
from collections import deque
from graph import Graph

def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    
    Returns:
        List of vertices forming the path, or None if no path exists
    """
    # TODO: Implement bfs_find_path
    # 1. Check if start or end is not in graph, return None if not
    # 2. Initialize a queue with (start, [start])
    # 3. Initialize visited set with start
    # 4. While queue is not empty, pop the queue
    # 5. If current vertex is end, return path
    # 6. For each neighbor of current, if not visited, add to queue and visited
    
    if start not in graph.vertices or end not in graph.vertices:
        return None
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    """
    Find all vertices reachable from start and their distances.
    
    Returns:
        Dict mapping vertex -> distance from start
    """
    # TODO: Implement bfs_all_reachable
    # 1. Check if start is not in graph, return empty dict if not
    # 2. Initialize distances dict with start at distance 0
    # 3. Initialize queue with start
    # 4. While queue is not empty, pop queue
    # 5. For each neighbor, if not in distances, set distance and add to queue
    
    if start not in graph.vertices:
        return {}
    distances = {start: 0}
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph.get_neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return distances

def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """Check if path exists between two vertices."""
    # TODO: Implement bfs_is_connected
    # 1. Use bfs_find_path to check if path exists
    # 2. Return True if path exists, False otherwise
    
    path = bfs_find_path(graph, v1, v2)
    return path is not None
