# Merge K Sorted Lists

> Merge K sorted lists into one sorted list efficiently. &nbsp;⏱ Time `O(n log k)` &nbsp;💾 Space `O(k)` where k = number of lists, n = total elements

## 🧠 The Idea

Use **divide and conquer**: pair up the K lists, merge each pair (using two-pointer merge), then repeat with the halved set of merged lists. Each round halves the number of lists, so there are O(log k) rounds, each touching n elements total → O(n log k).

```
Round 1: [L1,L2,L3,L4] → merge(L1,L2), merge(L3,L4)
Round 2: [M12, M34]     → merge(M12, M34)
Done!
```

## 📊 Visual

```
Lists: [1,4,8] [0,2,5] [3,6,9]

Round 1:
  merge([1,4,8], [0,2,5]) → [0,1,2,4,5,8]
  [3,6,9] has no pair → pass through

Round 2:
  merge([0,1,2,4,5,8], [3,6,9]) → [0,1,2,3,4,5,6,8,9]

Answer: [0,1,2,3,4,5,6,8,9] ✓
```

## 📜 History & Background

Merging sorted lists is the core operation of **merge sort** (von Neumann, 1945). The K-way merge with a heap is used in **external sorting** — sorting data too large to fit in memory (database engines, MapReduce, search index building).

## 💼 Tech Interview Tips

- **Heap approach** (most common answer): use a min-heap seeded with the first element of each list. Pop the minimum, push its successor. O(n log k). Great for streaming/large-k cases.
- **Divide & conquer** (shown here): elegant and O(n log k) — good if lists are given as arrays
- Naive approach (merge one by one): O(nk) — mention it but avoid it
- LeetCode 23 (with linked list nodes) — same idea, different data structure
- Know both heap and D&C approaches

## 🎯 Common Use Cases

- External merge sort (sorting files larger than RAM)
- Merging results from distributed database shards
- Combining sorted log streams from multiple servers
- MapReduce reduce phase
- Search engine index merging

## 🔗 Related Problems

- [Merge Sorted](../merge_sorted/) — merge two sorted arrays (the building block)
- [Heap](../heap/) — heap-based O(n log k) alternative
- [Topo Sort](../topo_sort/) — another multi-list problem
