# Lab 6: Breadth-First Search

## Student Information
- **Name:** Gretchen Allen
- **Date:** 03/05/2026

## Graph Concepts

### Adjacency List Representation
An adjacency list uses a graph of nodes that each maintain a list of its neighbors. Our graph uses a dictionary in which each of the keys are a node of the graph. Each key points to a list, and the list contains all nodes connected to that node by an edge.

### BFS Algorithm Steps
1. Initialize data structures (queue and visited set)
2. Process the queue (deque, check for goal)
3. Explore neighbors (if neighbor hasnt been visited, mark as visited; enqueue neighbor along with path expanded to include this neighbor)
4. Termination (if queue is empty and goal not found, return None)

## Test Results

| Start | End | Path | Edges |
|-------|-----|------|-------|
| Houston | El Paso |Houston -> San Antonio -> El Paso |2 |
| Houston | McKinney |Houston -> Dallas -> Plano -> McKinney |3 |
| Dallas | Laredo |Dallas -> Houston -> San Antonio -> Laredo |3 |

## Reflection Questions

1. Why does BFS use a queue instead of a stack?
A queue utilizes the first in, first out principle which ensures that the shortest path to each node will be found, since each level of the graph will be explored completely before moving to the next level. A stack, on the other hand, uses the last in, first out method which results in depth first exploration and is not well suited to cases such as this lab.

2. What's the difference between BFS shortest path and actual shortest distance?
The BFS shortest path depends only on the number of nodes and edges, and doesn't consider whether the edges are weighted when finding the minimal edges to reach the destination. The actual shortest distance takes into account any weights or distances that are associated with edges in order to minimize aspects such as travel costs. 

3. When would you use BFS vs DFS?
BFS is useful when you need to find the shortest path in unweighted graphs or explore nodes level by level, and DFS is better for applications which require deep exploration such as finding cycles in your graph or topological sorting.
