# Shortest Path

> Find the shortest path between two nodes in a graph. &nbsp;⏱ Unweighted: `O(V+E)` · Weighted (Dijkstra): `O((V+E) log V)` &nbsp;💾 Space `O(V)`

## 🧠 The Idea

- **Unweighted graph** → **BFS** guarantees the shortest path (fewest hops) because it explores nodes level by level.
- **Weighted graph (non-negative weights)** → **Dijkstra's algorithm** uses a min-heap to always expand the cheapest known node.
- **Negative weights** → **Bellman-Ford** relaxes all edges V-1 times.

```
BFS shortest path:
  queue = [(start, [start])]   ← (node, path_so_far)
  while queue:
      node, path = dequeue
      if node == target: return path
      for neighbour in graph[node]:
          if not visited: enqueue (neighbour, path + [neighbour])
```

## 📊 Visual

```
Graph (unweighted):        BFS from A to F:
    A                       Level 0: A
   / \                      Level 1: B, C
  B   C                     Level 2: D, E, F ← found F!
 / \   \
D   E   F                  Shortest path: A → C → F (2 hops)

Weighted graph (Dijkstra):
  A --1-- B --4-- D
  |               |
  2               1
  |               |
  C ------3------ D
                         Dijkstra expands cheapest node first using heap
```

## 📜 History & Background

- **BFS** for shortest path: Konrad Zuse (1945), Moore (1959)
- **Dijkstra's algorithm**: Edsger W. Dijkstra (1956, published 1959) — one of the most elegant algorithms in CS
- **Bellman-Ford**: Richard Bellman (1958), Lester Ford Jr. (1956)
- **A\***: Hart, Nilsson, Raphael (1968) — adds a heuristic to guide Dijkstra toward the goal

## 💼 Tech Interview Tips

| Graph Type | Algorithm | Time |
|---|---|---|
| Unweighted | BFS | O(V+E) |
| Non-negative weights | Dijkstra | O((V+E) log V) |
| Negative weights | Bellman-Ford | O(VE) |
| Grid (unit cost) | BFS | O(m·n) |
| All-pairs | Floyd-Warshall | O(V³) |

- For **grids**, BFS is almost always the answer
- Dijkstra requires a min-heap (`heapq`) — each node is `(cost, node_id)`

## 🎯 Common Use Cases

- GPS turn-by-turn navigation
- Network routing protocols (OSPF uses Dijkstra)
- Game pathfinding (A\* is standard in game engines)
- Social network "shortest connection path"
- Internet packet routing

## 🔗 Related Problems

- [BFS](../bfs/) — BFS for unweighted shortest path
- [Grid Traversal](../grid_traversal/) — shortest path in a maze
- [Topo Sort](../topo_sort/) — longest path in DAG via topological sort
- [Heap](../heap/) — min-heap used in Dijkstra
