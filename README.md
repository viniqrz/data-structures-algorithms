# 🧠 Data Structures & Algorithms

> A personal collection of classic algorithms and data structure problems — with clear implementations and quick-reference docs for interview prep.

Each problem lives in its **own folder** with:
- ✅ A Python implementation
- 📖 A `README.md` with the core idea, visual diagram, history, interview tips, and use cases

---

## 🗺️ Quick Navigation

### 🔍 Searching & Graph Traversal

| Problem | Time | Space | Key Pattern |
|---|---|---|---|
| [BFS](./bfs/) | O(V+E) | O(V) | Queue, level-by-level |
| [DFS](./dfs/) | O(V+E) | O(V) | Recursion / stack |
| [Binary Search](./binary_search/) | O(log n) | O(1) | Divide sorted range |
| [Grid Traversal](./grid_traversal/) | O(m·n) | O(m·n) | BFS/DFS on 2D matrix |
| [Shortest Path](./shortest_path/) | O(V+E) | O(V) | BFS (unweighted) |

### 🔀 Sorting

| Problem | Time | Space | Key Pattern |
|---|---|---|---|
| [Bucket Sort / Top-K Frequent](./bucket_sort/) | O(n) | O(n) | Frequency buckets |
| [Cyclic Sort](./cyclic_sort/) | O(n) | O(1) | Place num at index num-1 |
| [Dutch National Flag](./dutch_national_flag/) | O(n) | O(1) | 3-pointer partition |
| [Sort Colors](./sort_colors/) | O(n) | O(1) | Counting sort |
| [Merge Sorted Arrays](./merge_sorted/) | O(n+m) | O(n+m) | Two pointers |
| [Merge K Sorted Lists](./merge_k_lists/) | O(n log k) | O(k) | Divide & conquer / heap |
| [Topological Sort](./topo_sort/) | O(V+E) | O(V) | DFS post-order + reverse |

### 🔗 Linked Lists

| Problem | Time | Space | Key Pattern |
|---|---|---|---|
| [Reverse Linked List](./reverse_linked_list/) | O(n) | O(1) | 3-pointer iteration |
| [Detect Cycle (Linked List)](./detect_cycle_linked_list/) | O(n) | O(1) | Floyd's tortoise & hare |
| [Rotate Linked List](./rotate_linked_list/) | O(n) | O(1) | Make circular, find new tail |

### 🌳 Trees & Graphs

| Problem | Time | Space | Key Pattern |
|---|---|---|---|
| [Detect Cycle (Graph)](./detect_cycle/) | O(V+E) | O(V) | DFS with visited set |
| [N Provinces](./n_provinces/) | O(n²) | O(n) | Connected components DFS |
| [Recursive Deps](./recursive_deps/) | O(V+E) | O(V) | Post-order DFS |
| [Longest Leaf (Tree Height)](./longest_leaf/) | O(n) | O(h) | Post-order DFS |
| [N-th Level Leafs](./n_leafs/) | O(n) | O(h) | DFS with depth |
| [House Robber III](./house_robber_3/) | O(n) | O(h) | Tree DP (skip/take pair) |

### 📈 Dynamic Programming

| Problem | Time | Space | Key Pattern |
|---|---|---|---|
| [Knapsack 0/1](./knapsack/) | O(n·W) | O(n·W) | Include/exclude DP |
| [Longest Consecutive Sequence](./longest_consecutive_sequence/) | O(n) | O(n) | Set + sequence root |
| [Longest Increasing Subsequence](./longest_increasing_subsequence/) | O(n²) | O(n) | DP / patience sort |
| [Longest Common Subsequence](./longest_common_subsequence/) | O(m·n) | O(m·n) | 2D DP |
| [Max Subarray (Kadane's)](./max_subarray/) | O(n) | O(1) | Extend or restart |

### 🪟 Sliding Window

| Problem | Time | Space | Key Pattern |
|---|---|---|---|
| [Longest Substring (No Repeat)](./longest_substring/) | O(n) | O(m) | Set + shrink left |
| [Character Replacement](./character_replacement/) | O(n) | O(1) | max_freq window trick |

### 🔤 Strings

| Problem | Time | Space | Key Pattern |
|---|---|---|---|
| [Is Anagram](./is_anagram/) | O(n) | O(1) | Counter comparison |
| [Is Palindrome](./is_palindrome/) | O(n) | O(1) | Two pointers |

### 🎲 Backtracking

| Problem | Time | Space | Key Pattern |
|---|---|---|---|
| [Combination Sum](./combination_sum/) | O(n^(t/m)) | O(t/m) | DFS include/skip (reuse OK) |
| [Combination Sum II](./combination_sum_2/) | O(2^n) | O(n) | Sort + skip duplicates |
| [Permutations](./permutations/) | O(n!·n) | O(n) | All orderings backtrack |
| [Subsets](./subsets/) | O(n·2^n) | O(n) | Include/exclude each element |

### 📦 Data Structures

| Problem | Time | Space | Key Pattern |
|---|---|---|---|
| [Heap / Priority Queue](./heap/) | O(log n) push/pop | O(n) | Min-heap, heapq |

### 🗺️ Arrays & Matrices

| Problem | Time | Space | Key Pattern |
|---|---|---|---|
| [Rotate 90°](./rotate_90/) | O(n²) | O(1) | Reverse rows + transpose |

---

## 🚀 How to Use This Repo

1. **Browse by category** using the table above
2. **Open any folder** — the `README.md` has the theory, the `.py` file has the code
3. **For interview prep**: read the README first for the key insight, then try to implement from memory

```
📁 problem-name/
   ├── problem.py     ← implementation
   └── README.md      ← explanation + interview tips
```

---

## 📚 Patterns to Master

| Pattern | Problems |
|---|---|
| **Two Pointers** | Palindrome, Merge Sorted, Dutch National Flag |
| **Sliding Window** | Longest Substring, Character Replacement |
| **BFS/DFS** | Graph traversal, Grid, Shortest Path, Connected Components |
| **Backtracking** | Subsets, Permutations, Combination Sum |
| **Dynamic Programming** | Knapsack, LCS, LIS, Max Subarray, House Robber |
| **Divide & Conquer** | Merge K Lists, Binary Search |
| **Topological Sort** | Topo Sort, Recursive Deps, Detect Cycle |

---

*Happy grinding! 🎯*

