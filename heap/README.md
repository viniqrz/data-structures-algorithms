# Heap / Priority Queue

> Always get the **min (or max)** element in `O(log n)`. &nbsp;⏱ Push/Pop `O(log n)` · Heapify `O(n)` &nbsp;💾 Space `O(n)`

## 🧠 The Idea

A heap is a **complete binary tree** stored in an array where every parent is ≤ its children (min-heap). This guarantees the smallest element is always at index 0. Push adds to the end and bubbles up; pop removes the root, puts the last element there, and sinks it down.

```
Python heapq is a min-heap:
  heapify(list)        → O(n) — convert list in-place
  heappush(h, val)     → O(log n)
  heappop(h)           → O(log n) — removes & returns smallest
  h[0]                 → O(1) — peek smallest

For max-heap: negate all values (-val)
```

## 📊 Visual

```
List: [3, 1, 2]   →   heapify   →   [1, 3, 2]

        1          ← root = min
       / \
      3   2

heappop() → returns 1, tree becomes [2, 3]
        2
       /
      3
```

## 📜 History & Background

The heap data structure was invented by **J.W.J. Williams** in 1964 as the basis for **Heapsort**. Python's `heapq` module exposes a min-heap interface, and it's one of the most battle-tested data structures in CS.

## 💼 Tech Interview Tips

- **"K largest/smallest"** elements → heap is usually optimal O(n log k)
- `heapify` is **O(n)**, not O(n log n) — interviewers love this fact
- Python only has min-heap; for max-heap **negate values** (`heappush(h, -val)`)
- Heap ≠ sorted array — siblings have no ordering guarantee, only parent < children
- Useful pattern: maintain a heap of size K while iterating → get top-K in O(n log k)

## 🎯 Common Use Cases

- **K closest points** to origin, K most frequent elements
- **Merge K sorted lists** — min-heap tracks current minimums
- **Dijkstra's algorithm** — always expand cheapest node
- **Task scheduling** — process by priority
- **Median in a data stream** — two heaps (max-heap of lower half, min-heap of upper half)

## 🔗 Related Problems

- [Merge K Lists](../merge_k_lists/) — classic heap application
- [Bucket Sort](../bucket_sort/) — O(n) alternative to heap for top-K frequent
- [Shortest Path](../shortest_path/) — Dijkstra uses a min-heap
