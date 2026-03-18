# Grid Traversal — BFS & DFS on 2D Matrices

> Traverse every cell in a grid using BFS (level-by-level) or DFS (depth-first). &nbsp;⏱ Time `O(m×n)` &nbsp;💾 Space `O(m×n)`

## 🧠 The Idea

A grid is just a **graph in disguise** — each cell `(i, j)` is a node, and its neighbours are the 4 adjacent cells (up/down/left/right, or diagonals for 8-directional). Apply BFS or DFS with a `visited` set of `(row, col)` tuples, and always **check bounds and visited** before processing.

```
Neighbours of (i, j):
  (i-1, j)  ← up
  (i+1, j)  ← down
  (i, j-1)  ← left
  (i, j+1)  ← right

Boundary check: 0 ≤ i < rows  and  0 ≤ j < cols
```

## 📊 Visual

```
Grid (4×6):
  0   1   2   3   4   5
  6   7   8   9  10  11
 12  13  14  15  16  17
 18  19  20  21  22  23

BFS from (0,0): visits row by row, left to right
  0 → 1 → 6 → 2 → 7 → 12 → ...   (by Manhattan distance from origin)

DFS from (0,0): dives deep before coming back
  0 → 1 → 2 → 3 → 4 → 5 → 11 → 17 → 23 → ...
```

## 📜 History & Background

Grid traversal is the two-dimensional generalisation of graph traversal, fundamental to **image processing** (flood fill), **pathfinding** (A\*, Dijkstra on grids), and **cellular automaton** simulation (Conway's Game of Life).

## 💼 Tech Interview Tips

- Template pattern: BFS for **shortest path** in grid, DFS for **exhaustive exploration** (islands, connected regions)
- Store visited as a set of `(i, j)` tuples **or** modify the grid in-place (`grid[i][j] = '#'` to mark visited — common trick to save space)
- **"Number of Islands"** (LeetCode 200) = count BFS/DFS calls from unvisited '1' cells
- Add boundary and visited checks **at dequeue time** (BFS) or at the **top of DFS** to handle edge cases cleanly
- For 4-directional movement: use `dirs = [(0,1),(0,-1),(1,0),(-1,0)]` and loop

## 🎯 Common Use Cases

- Number of islands / connected regions (LeetCode 200, 695)
- Shortest path in a maze (BFS — LeetCode 1091)
- Flood fill (image paint bucket tool — LeetCode 733)
- Game grid pathfinding (Pac-Man, chess, Minesweeper)
- Rotten oranges / spreading problems (multi-source BFS)

## 🔗 Related Problems

- [BFS](../bfs/) — the general BFS algorithm
- [DFS](../dfs/) — the general DFS algorithm
- [Shortest Path](../shortest_path/) — BFS for shortest path
- [N Provinces](../n_provinces/) — connected components in a graph
