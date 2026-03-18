# Permutations — Backtracking

> Generate **all possible orderings** of a list of distinct integers. &nbsp;⏱ Time `O(n! · n)` &nbsp;💾 Space `O(n)`

## 🧠 The Idea

Use **backtracking**: build the permutation incrementally. At each step, try adding each unused element to the current partial permutation. When the permutation is complete (length n), record it. Then backtrack — remove the last element and try the next option.

```
Algorithm:
  def backtrack():
      if len(perm) == n:
          result.append(perm.copy())
          return
      for x in nums:
          if x not in perm:
              perm.append(x)
              backtrack()
              perm.pop()  ← backtrack
```

## 📊 Visual

```
nums = [1, 2, 3]

                    []
          /          |          \
        [1]         [2]         [3]
       /   \       /   \       /   \
    [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
      |     |     |     |     |     |
  [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]

6 = 3! permutations ✓
```

## 📜 History & Background

Permutation generation is fundamental to combinatorics. **Heap's algorithm** (B. R. Heap, 1963) generates all permutations with minimal swaps. **Steinhaus–Johnson–Trotter algorithm** generates permutations where each step is a single adjacent swap — used in combinatorial testing and Gray codes.

## 💼 Tech Interview Tips

- n! grows extremely fast: 10! = 3,628,800 — only feasible for small n (≤12)
- Use `x not in perm` check (O(n)) or a separate `used` boolean array (O(1)) for better performance
- `perm.copy()` is essential — lists are mutable, so you must snapshot before appending to results
- **Permutations II** (with duplicates): sort first, use a `used` boolean array, skip `if i > 0 and nums[i] == nums[i-1] and not used[i-1]`
- LeetCode 46 (distinct), LeetCode 47 (with duplicates)

## 🎯 Common Use Cases

- Generating all possible orderings for testing (combinatorial test cases)
- Password generation / brute-force cracking analysis
- Scheduling all possible task orderings
- Travelling Salesman Problem (brute-force baseline)
- Anagram generation

## 🔗 Related Problems

- [Combination Sum](../combination_sum/) — ordered selections with sum constraint
- [Subsets](../subsets/) — unordered subsets (no full permutation needed)
- [Combination Sum II](../combination_sum_2/) — handle duplicates pattern
