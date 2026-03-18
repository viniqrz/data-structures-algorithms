# Merge Two Sorted Arrays

> Combine two sorted arrays into one sorted array. &nbsp;⏱ Time `O(n+m)` &nbsp;💾 Space `O(n+m)`

## 🧠 The Idea

Use **two pointers** — one for each array. At each step, pick the smaller of the two current elements and append it to the result. When one array is exhausted, append the remainder of the other.

```
Algorithm:
  p1, p2 = 0, 0
  while p1 < len(a) or p2 < len(b):
      if p1 exhausted: take from b
      elif p2 exhausted: take from a
      elif a[p1] <= b[p2]: take a[p1]; p1++
      else: take b[p2]; p2++
```

## 📊 Visual

```
a = [1, 4, 6, 8]
b = [2, 3, 5, 7]
    p1            p2

Compare 1 vs 2 → take 1 (p1++)
Compare 4 vs 2 → take 2 (p2++)
Compare 4 vs 3 → take 3 (p2++)
Compare 4 vs 5 → take 4 (p1++)
Compare 6 vs 5 → take 5 (p2++)
Compare 6 vs 7 → take 6 (p1++)
Compare 8 vs 7 → take 7 (p2++)
b exhausted     → take 8

Result: [1, 2, 3, 4, 5, 6, 7, 8] ✓
```

## 📜 History & Background

Merging is the **combine** step of merge sort, invented by **John von Neumann** in 1945. It's also the foundation of database **sort-merge join** — a standard join algorithm when both input relations are sorted on the join key.

## 💼 Tech Interview Tips

- **In-place merge** (LeetCode 88): fill `nums1` from the back (no extra space needed) — iterate from the ends
- Two-pointer merge is O(n+m) time and O(n+m) space; in-place is O(1) extra space
- This is the **merge step** in merge sort — know it cold
- Classic interview question: merge `nums2` into `nums1` in-place given enough space

## 🎯 Common Use Cases

- Merge sort combine step
- Database sort-merge join
- Combining sorted results from multiple search indexes
- Real-time stream merging (e.g., sensor data from two sorted streams)

## 🔗 Related Problems

- [Merge K Lists](../merge_k_lists/) — generalisation to K arrays
- [Binary Search](../binary_search/) — works on sorted arrays
- [Dutch National Flag](../dutch_national_flag/) — sorting by categories
