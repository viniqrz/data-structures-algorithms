# Longest Consecutive Sequence

> Find the length of the longest sequence of consecutive integers in an **unsorted** array. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(n)`

## 🧠 The Idea

Convert the array to a **set** for O(1) lookups. Then, for each number, only start counting if it's the **beginning of a sequence** (i.e., `n-1` is not in the set). Count how many consecutive numbers follow it. This ensures each number is processed at most once.

```
Algorithm:
  nums_set = set(nums)
  for n in nums_set:
      if n - 1 not in nums_set:   ← sequence start!
          count = 0
          while n + count in nums_set:
              count += 1
          max_len = max(max_len, count)
```

## 📊 Visual

```
nums = [100, 4, 200, 1, 3, 2]
set   = {1, 2, 3, 4, 100, 200}

n=100: 99 not in set → start counting: 100 → len=1
n=4:   3 IS in set   → skip (not start)
n=200: 199 not in set → start: 200 → len=1
n=1:   0 not in set  → start: 1→2→3→4 → len=4  ← MAX
n=3:   2 IS in set   → skip
n=2:   1 IS in set   → skip

Answer: 4 ✓
```

## 📜 History & Background

This is **LeetCode 128** (Hard). The O(n) solution is a great example of how converting to a set and thinking about "sequence starts" turns an apparently O(n²) problem into O(n). It's a common interview question at top tech companies.

## 💼 Tech Interview Tips

- The naive approach is O(n²) — sort or check each number for next. The set approach is O(n)
- Key insight: **only start counting from sequence roots** (`n-1 not in set`) to avoid redundant work
- Handles duplicates naturally (set deduplicates)
- Total inner-loop iterations across all outer-loop iterations = O(n) (each number counted at most once)
- Edge cases: empty array → 0, single element → 1

## 🎯 Common Use Cases

- Finding streaks in activity data (consecutive login days)
- Range detection in logs or time-series data
- Database query optimisation (finding gaps in sequences)
- Detecting consecutive IDs in records

## 🔗 Related Problems

- [Longest Increasing Subsequence](../longest_increasing_subsequence/) — increasing (not necessarily consecutive)
- [Cyclic Sort](../cyclic_sort/) — O(n) sort exploiting range 1..n
- [Binary Search](../binary_search/) — searching in sorted sequences
