# Breadth-First Search (BFS)

> Explore a graph **level by level** using a queue. &nbsp;⏱ Time `O(V+E)` &nbsp;💾 Space `O(V)`

## 🧠 The Idea

BFS starts at a source node and visits **all its neighbours first**, then their neighbours, and so on — like ripples spreading across water. It uses a **queue (FIFO)** to keep track of nodes to visit next, and a **visited set** to avoid revisiting.

```
Algorithm:
  1. Enqueue start node, mark visited
  2. While queue is not empty:
       node = dequeue
       process node
       for each unvisited neighbour: enqueue + mark visited
```

## 📊 Visual

```
Graph:          BFS from A (queue snapshots):
    A
   / \           [A]  → visit A, enqueue B, C
  B   C          [B, C]  → visit B, enqueue D, E
 / \   \         [C, D, E]  → visit C, enqueue F
D   E   F        [D, E, F]  → ...
                 Order: A → B → C → D → E → F
```

## 📜 History & Background

BFS was first described by **Konrad Zuse** in his 1945 thesis, then independently published by **Edward F. Moore** in 1959 for maze-solving. It became a cornerstone of graph theory and computer science.

## 💼 Tech Interview Tips

- **Shortest path** in an unweighted graph? → BFS is your answer (DFS won't guarantee shortest)
- Use `collections.deque` — `list.pop(0)` is O(n), deque is O(1)
- Always maintain a `visited` set; add to it **when enqueuing**, not when dequeuing (avoids duplicate enqueues)
- **Level-order tree traversal** is just BFS on a tree
- If asked for "minimum steps / hops", think BFS first

## 🎯 Common Use Cases

- Shortest path in unweighted graphs (GPS, network routing)
- Social network "degrees of separation" (LinkedIn connections)
- Web crawlers exploring pages by link depth
- Word Ladder / sliding puzzle problems
- Finding all nodes within distance K

## 🔗 Related Problems

- [DFS](../dfs/) — depth-first alternative
- [Grid Traversal](../grid_traversal/) — BFS/DFS on 2D matrices
- [Shortest Path](../shortest_path/) — BFS for unweighted shortest path
- [N Provinces](../n_provinces/) — connected components with DFS/BFS
