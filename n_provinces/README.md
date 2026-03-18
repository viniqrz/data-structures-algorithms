# Number of Provinces — Connected Components

> Count the number of **connected components** in an undirected graph given as an adjacency matrix. &nbsp;⏱ Time `O(n²)` &nbsp;💾 Space `O(n)`

## 🧠 The Idea

Iterate over all cities. If a city hasn't been visited, it's the start of a **new province** (connected component) — increment the count and DFS/BFS from it to mark all cities in the same province as visited.

```
Algorithm:
  for city in range(n):
      if not visited[city]:
          count += 1
          dfs(city)   ← marks all connected cities as visited
```

## 📊 Visual

```
isConnected = [[1,1,0],   City 0 ─── City 1      City 2 (isolated)
               [1,1,0],
               [0,0,1]]

DFS from city 0:
  → visits city 1 (connected[0][1]=1)
  → city 1's neighbours: city 0 (visited), no others
  Province 1: {0, 1}

DFS from city 2 (unvisited):
  Province 2: {2}

Total provinces = 2 ✓

isConnected = [[1,0,0],   City 0    City 1    City 2 (all isolated)
               [0,1,0],
               [0,0,1]]
→ 3 provinces ✓
```

## 📜 History & Background

Counting connected components is a foundational graph theory problem. **Union-Find** (Disjoint Set Union), developed by Tarjan and others in the 1970s, offers an efficient alternative with near-O(n) time. LeetCode 547 — a Medium-level problem popular in FAANG interviews.

## 💼 Tech Interview Tips

- Same pattern as **Number of Islands** (LeetCode 200) — just on adjacency matrix vs grid
- **Union-Find** is the alternative: for each `isConnected[i][j]==1`, union(i,j), then count roots → O(n²·α(n))
- The adjacency matrix is symmetric → only need to check upper triangle
- Generalises easily: weighted connections, threshold-based provinces, k-hop neighbours

## 🎯 Common Use Cases

- Social network community detection
- Network connectivity analysis (is every router reachable?)
- Geographic clustering (which cities are in the same region?)
- Circuit connectivity verification

## 🔗 Related Problems

- [Grid Traversal](../grid_traversal/) — connected components on a 2D grid
- [DFS](../dfs/) — the traversal algorithm used
- [BFS](../bfs/) — alternative traversal
- [Detect Cycle](../detect_cycle/) — another graph problem
