# Traveling Salesman (TSP)

> Find the minimum cost to visit every city exactly once. &nbsp;⏱ Current implementation: `O(N * N!)` &nbsp;💾 Space `O(N)` recursion depth

## 🧠 The Idea

This implementation uses DFS to explore every valid path that visits all nodes exactly once, then returns the minimum total distance.

- It starts DFS from each node.
- It tracks the current path and running distance.
- If a node repeats before covering all nodes, that branch is invalid.
- If a branch visits all nodes, its distance becomes a candidate answer.

```text
dfs(node, distance, path):
    if node already in path: return inf
    add node to path
    if path includes all nodes: return distance
    return min(dfs(neighbour, distance + w, path_copy) for neighbour)
```

Note: This code computes the shortest Hamiltonian path variant (no forced return to start), not the classic TSP cycle.

## 📊 Visual

```text
Graph:
    A --2-- B
    | \     |
    1  2    3
    |    \  |
    C --1-- D

Try starts at A, B, C, D and take minimum valid full-visit path.
One optimal result here: B -> A -> C -> D = 2 + 1 + 1 = 4
```

## 📜 History & Background

The Traveling Salesman Problem is one of the most famous NP-hard optimization problems. It appears in logistics, chip manufacturing, robotics, and route planning. Because exact search scales poorly, practical systems usually rely on dynamic programming for moderate sizes or approximation/heuristic algorithms for large sizes.

## 💼 Tech Interview Tips

- Clarify whether the question expects a Hamiltonian path or a cycle (must return to start).
- Brute-force DFS/backtracking is acceptable for small `N` and good for explaining state-space search.
- A classic optimization is DP + bitmask: `O(N^2 * 2^N)`.
- If revisits are allowed or weights are non-complete, this is no longer standard TSP.
- Mention pruning opportunities (current distance already worse than known best).

## 🎯 Common Use Cases

- Delivery route planning
- PCB drilling and CNC tool path optimization
- Warehouse picking optimization
- Robotics task sequencing
- DNA fragment ordering (related formulations)

## 🔗 Related Problems

- [DFS](../dfs/) - traversal foundation used here
- [Shortest Path](../shortest_path/) - shortest route between two nodes (different from visiting all nodes)
- [Topo Sort](../topo_sort/) - ordering constraints in DAGs
- [Knapsack](../knapsack/) - another classic combinatorial optimization problem
