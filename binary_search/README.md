# Binary Search

> Find a target in a **sorted** array by halving the search space each step. &nbsp;⏱ Time `O(log n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

If the array is sorted, you can eliminate **half** the remaining elements at each step. Check the middle element — if it equals the target you're done; if the target is larger, discard the left half; if smaller, discard the right half. Repeat until found or the search space is empty.

```
Algorithm:
  left, right = 0, len(array) - 1
  while left <= right:
      mid = (left + right) // 2
      if array[mid] == target: return mid
      elif target > array[mid]: left = mid + 1
      else: right = mid - 1
  return -1   # not found
```

## 📊 Visual

```
Array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   Target: 9
        L                           R
Step 1: mid=5 → value=6 → 9>6 → move L right
                               L         R
Step 2: mid=8 → value=9 → FOUND at index 8  ✓

Only 2 comparisons for 10 elements!
(vs. up to 10 comparisons with linear search)
```

## 📜 History & Background

Binary search was first described by **John Mauchly** in 1946. Despite its simplicity, a bug-free implementation is notoriously tricky — Jon Bentley noted in 1986 that most textbook implementations had bugs. The modern `left + (right - left) // 2` form avoids integer overflow.

## 💼 Tech Interview Tips

- Array **must be sorted** — if not, sort first (adds O(n log n))
- Use `left <= right` (not `<`) to handle single-element arrays correctly
- Prefer `mid = left + (right - left) // 2` in languages with integer overflow (Python is fine with `//`)
- Know the **3 variants**: exact match, find first occurrence, find insert position
- Binary search applies beyond arrays: search on **answer space** (e.g., "minimum speed to finish tasks")

## 🎯 Common Use Cases

- Searching in sorted databases / dictionaries
- Finding the insert position (`bisect` module in Python)
- Rotated sorted array search (LeetCode 33)
- "Minimum/maximum feasible value" problems (binary search on answer)
- Square root / power approximations

## 🔗 Related Problems

- [Merge Sorted](../merge_sorted/) — maintains sorted order
- [Longest Increasing Subsequence](../longest_increasing_subsequence/) — O(n log n) variant uses binary search
