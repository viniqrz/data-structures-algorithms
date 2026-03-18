# Subsets — Power Set

> Generate **all possible subsets** (the power set) of a list of distinct integers. &nbsp;⏱ Time `O(n · 2^n)` &nbsp;💾 Space `O(n)`

## 🧠 The Idea

Use **backtracking/DFS**: at each index, make two choices — **include** the element or **exclude** it. When you've decided for all elements (index reaches end of list), record the current subset. This produces exactly 2^n subsets.

```
Algorithm:
  def dfs(i):
      if i >= len(nums):
          result.append(subset.copy())
          return
      subset.append(nums[i]); dfs(i+1)   ← include
      subset.pop();            dfs(i+1)   ← exclude
```

## 📊 Visual

```
nums = [1, 2, 3]

Decision tree (include left, exclude right):
                  []
            /           \
          [1]            []
        /     \        /     \
      [1,2]  [1]    [2]      []
      / \    / \    / \      / \
[1,2,3][1,2][1,3][1][2,3][2][3][]

2^3 = 8 subsets:
[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] ✓
```

## 📜 History & Background

The power set concept dates to **Georg Cantor's** set theory (1874). In CS, the bitmask representation of subsets (each bit = include/exclude) is foundational to **dynamic programming on subsets** (e.g., Travelling Salesman DP, bitmask DP). LeetCode 78.

## 💼 Tech Interview Tips

- There are always exactly **2^n** subsets — good sanity check
- **Bitmask alternative**: iterate `0` to `2^n - 1`; bit `k` set means include element `k` → elegant but less flexible
- **Subsets II** (LeetCode 90, with duplicates): sort first, skip duplicates at same DFS level
- `subset.copy()` is essential — don't append the mutable `subset` reference
- Subsets is often the basis for more complex backtracking: combine with a sum constraint → Combination Sum

## 🎯 Common Use Cases

- Feature selection in machine learning (try all feature subsets)
- Generating all possible test configurations
- Combinatorial optimisation (try all subsets for small n)
- Menu/option combinations
- Bit manipulation tricks in competitive programming

## 🔗 Related Problems

- [Combination Sum](../combination_sum/) — subsets with a sum target
- [Permutations](../permutations/) — ordered arrangements
- [Combination Sum II](../combination_sum_2/) — subsets with duplicates handling
- [Knapsack](../knapsack/) — DP over all subsets implicitly
