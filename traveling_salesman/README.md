# Traveling Salesman (TSP)

> Visit every node exactly once with minimum total cost. &nbsp;⏱ Current approach: `O(N * N!)` &nbsp;💾 Space `O(N)` recursion depth

## 🧠 The Idea

This implementation performs DFS from every possible start node and takes the minimum valid full-visit distance.

- A path is invalid if it revisits a node before all nodes are covered.
- A path is complete when it contains every node exactly once.
- Dead ends return `inf`, so they are naturally ignored by `min(...)`.

```text
Algorithm:
  1. For each node as start:
       run DFS(node, distance=0, path=[])
  2. DFS tries every outgoing edge to unvisited nodes
  3. If path size == total nodes: return distance
  4. Return global minimum over all starts
```

Note: This code solves the shortest Hamiltonian **path** variant (no mandatory return to start), not the classic Hamiltonian **cycle** TSP.

## 📊 Visual

```text
Graph:
    A --2-- B
    | \     |
    1  2    3
    |    \  |
    C --1-- D

DFS tries starts at A, B, C, D.
Best full-visit path: B -> A -> C -> D
Cost: 2 + 1 + 1 = 4
```

## 📜 History & Background

TSP is one of the best-known NP-hard optimization problems. It appears in logistics, robotics, manufacturing, and scheduling. Exact brute-force search becomes infeasible quickly, so practical solutions use dynamic programming, branch-and-bound, or approximation/heuristic methods.

## 💼 Tech Interview Tips

- Clarify constraints first: path vs cycle, directed vs undirected, complete vs sparse graph.
- Backtracking DFS is great for small `N` and for explaining pruning strategies.
- Standard optimization: DP with bitmask (`O(N^2 * 2^N)`).
- Keep an eye on base cases and invalid branches (`inf` pattern is common).
- If the interviewer asks for "return to start", add final edge check/cost.

## 🎯 Common Use Cases

- Delivery and routing optimization
- CNC/PCB tool movement planning
- Warehouse picking sequence optimization
- Robotics waypoint sequencing
- Crew/job scheduling with transition costs

## 🔗 Related Problems

- [DFS](../dfs/) - traversal strategy used in this solution
- [Shortest Path](../shortest_path/) - shortest route between two nodes (different objective)
- [Topological Sort](../topo_sort/) - ordering tasks under dependencies
- [Knapsack](../knapsack/) - classic combinatorial optimization
