# Dutch National Flag — Three-Way Partition

> Sort an array of 0s, 1s, and 2s **in one pass** with O(1) space. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

Maintain three regions using pointers `low`, `mid`, `high`:
- `[0, low)` → all 0s
- `[low, mid)` → all 1s
- `(high, n-1]` → all 2s
- `[mid, high]` → unknown (to be processed)

Process elements at `mid`: swap 0s to the front, 2s to the back, leave 1s in place.

```
if nums[mid] == 0: swap(low, mid); low++; mid++
if nums[mid] == 1: mid++
if nums[mid] == 2: swap(mid, high); high--  ← don't increment mid!
```

## 📊 Visual

```
Input: [2, 0, 1, 2, 1, 0]
        L=M           H

Step 1: nums[mid]=2 → swap(mid,high) → [0, 0, 1, 2, 1, 2], H--
Step 2: nums[mid]=0 → swap(low,mid) → [0, 0, 1, 2, 1, 2], L++, M++
...

Result: [0, 0, 1, 1, 2, 2] ✓

Regions:   |0 0|1 1|2 2|
            low  mid  high
```

## 📜 History & Background

Proposed by **Edsger W. Dijkstra** (1976) in his book *A Discipline of Programming*, inspired by the three-coloured Dutch national flag 🇳🇱. It's a special case of **3-way partition** used in quicksort implementations (especially for arrays with many duplicate keys — "Dutch National Flag Quicksort").

## 💼 Tech Interview Tips

- The key subtlety: when swapping a 2 to the back, **don't increment `mid`** — the swapped-in value is unknown and needs to be evaluated
- When swapping a 0 to the front, it's safe to increment both `low` and `mid` (we know we put a 1 or 0 in the mid spot)
- Generalises to **k-way partition** for k distinct values
- LeetCode 75 — "Sort Colors"
- Also check out [Sort Colors](../sort_colors/) which uses a two-pass counting approach instead

## 🎯 Common Use Cases

- 3-way partition in quicksort (handles duplicates efficiently)
- Sorting low/medium/high priority task queues
- Segregating elements into 3 categories in one pass
- Database query result ranking (low/med/high relevance)

## 🔗 Related Problems

- [Sort Colors](../sort_colors/) — two-pass counting approach to same problem
- [Cyclic Sort](../cyclic_sort/) — O(n) sort for 1..n range
- [Merge Sorted](../merge_sorted/) — another two-pointer sorting technique
