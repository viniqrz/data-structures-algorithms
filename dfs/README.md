# Depth-First Search (DFS)

> Explore a graph by diving **as deep as possible** before backtracking. &nbsp;⏱ Time `O(V+E)` &nbsp;💾 Space `O(V)`

## 🧠 The Idea

DFS picks a start node and keeps going **deeper along one path** until it hits a dead end, then backtracks to explore other branches. It can be implemented **recursively** (using the call stack) or **iteratively** (using an explicit stack).

```
Algorithm (recursive):
  1. Mark current node as visited
  2. Process node
  3. For each unvisited neighbour: recurse
```

## 📊 Visual

```
Graph:          DFS from A (recursive):
    A
   / \           Visit A → go to B
  B   C          Visit B → go to D
 / \   \         Visit D (leaf) → backtrack to B
D   E   F        Visit E → go to F
                 Visit F (leaf) → backtrack...
                 Order: A → B → D → E → F → C
```

## 📜 History & Background

DFS has roots in 19th-century maze-solving algorithms (Trémaux's algorithm, ~1882). It was formally analyzed for graphs by **Tarjan** and others in the 1970s, leading to efficient algorithms for SCCs and bridges.

## 💼 Tech Interview Tips

- DFS is naturally recursive — draw the **recursion tree** to reason about it
- For **cycle detection** in a directed graph, track nodes in the current recursion stack (not just visited)
- **Topological sort** = DFS post-order + reverse
- Watch for **stack overflow** on huge inputs — consider iterative DFS
- DFS explores *one* full path first; BFS explores all paths equally — know when to use which

## 🎯 Common Use Cases

- Cycle detection in directed/undirected graphs
- Topological ordering (build systems, task schedulers)
- Finding connected components
- Tree traversals (pre/in/post-order are all DFS variants)
- Maze generation and solving

## 🔗 Related Problems

- [BFS](../bfs/) — breadth-first alternative
- [Topological Sort](../topo_sort/) — DFS post-order application
- [Detect Cycle](../detect_cycle/) — cycle detection in directed graph
- [N Provinces](../n_provinces/) — connected components
- [Recursive Deps](../recursive_deps/) — dependency resolution via DFS
