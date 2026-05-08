# Lab Report #9 — Dijkstra's Shortest Path

Student Information

## Name: Gretchen Allen
## Date: 4/11/2026
## Algorithm Analysis: Dijkstra's Algorithm

What type of graph does this program build? 

Undirected, weighted

Why must all edge weights be non-negative for Dijkstra's to work? 

Dijkstra's algorithm assumes that once a node has been processed, there is no need to revisit that node since the shortest path has already been found. With negative weights, a later update with a negative edge could reduce a previously finalized shortened path. Also, negative weights could create cycles that continuously decrease the path cost, leading to incorrect results or infinite loops.

Time Complexity (with simple array scan for min-node): O(n^2)

Time Complexity (with a min-heap/priority queue): O((n+e)/log n)

Core Data Structures

Structure	Variable Name	What It Stores
Adjacency dict	graph	
Cost table	costs	
Parent table	parents	
Visited list	processed	
Algorithm Trace

Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D:

Iteration	Current Node	costs[A]	costs[B]	costs[C]	costs[D]	processed
Init	—					
1						
2						
3						
4						
Shortest path A to D: A -> B -> C -> D
Total cost: 6

Reflection Questions

Why does the algorithm initialize all node costs to infinity except the start node?
Using infinity for all initial node costs simplifies the code needed to run Dijkstra's algorithm. If all the nodes started with zero, distinguising between reachable and unreachable nodes for the purpose of updating the shortest known path would be complex. Also, the start node is initialized to zero to ensure that this is where the algorithm begins processing the nodes.

Why do we store edges in both directions (graph[a][b] and graph[b][a])? What would break if we only stored one direction?
Storing edges in both directions ensures that the algorithm can explore all possible paths correctly. If only one direction were stored, the graph would function like a directed graph and you would lose the ability to traverse back and forth between nodes, which is essential for accurately representing an undirected graph.

The find_lowest_cost_node() function scans all nodes linearly. How would using a priority queue (min-heap) improve performance, and why does it matter for large graphs?
A priority queue would improve the overall time complexity from O(n^2) to O((n+e)/log n). In a large graph, this difference in time complexity would significantly reduce the processing time and make the algorithm more scalable.

If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights?
Dijkstra's algorithm assumes that once a node has been processed, there is no need to revisit it since the shortest path has already been found. With a negative edge weight, this might not be true since a previously finalized path could be further reduced. The algorithm that can handle negative weights is the Bellman-Ford algorithm.

How does the parents dictionary allow path reconstruction? Why do we reverse the path at the end?
The parents dictionary keeps track of each node that was the previous node on the shortest path of the graph. This allows you to "walk backward" from the destination node to the start node by following the chain of parent nodes. This results in a path that runs from the end to the start, which is why the path is reversed at the end. This gives the correct order of start to end.

What happens when the source and destination are in disconnected components of the graph? How does the code detect this?
Dijkstra's algorithm cannot find a path between a source and destination that are disconnected. Since the cost of all nodes are initialized to infinity, the destination node will remain at infinite cost after the algorithm completes. The algorithm will return none, indicating that there is no path from the source to the destination.
