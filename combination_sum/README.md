# Combination Sum — Backtracking

> Find all combinations of numbers that **sum to a target**, reusing elements freely. &nbsp;⏱ Time `O(n^(t/m))` &nbsp;💾 Space `O(t/m)`

## 🧠 The Idea

Use **backtracking** — build combinations incrementally and abandon ("backtrack") paths that can't lead to a solution. At each step, you have two choices: **include** the current element (stay at same index, since reuse is allowed) or **skip** to the next element.

```
Algorithm:
  def backtrack(index, current_total):
      if total == target: record solution
      if total > target or index out of bounds: return

      include nums[i]: backtrack(i, total + nums[i])   # reuse OK
      exclude nums[i]: backtrack(i+1, total)            # move on
```

## 📊 Visual

```
nums = [2, 3, 6, 7],  target = 7

Decision tree (showing include/skip at each level):
              []
         /         \
       [2]          []
      /    \        / \
   [2,2]  [2]    [3]  []
   /  \    ...   ...  [7]✓
[2,2,2] [2,2,3]✓
  /
[2,2,2,2](>7)✗

Solutions: [2,2,3], [7]
```

## 📜 History & Background

Combination sum is **LeetCode 39**, a foundational backtracking problem. Backtracking itself dates to the 1950s (used in early constraint satisfaction solvers and game trees).

## 💼 Tech Interview Tips

- Draw the **decision tree** on paper first — it makes the recursion obvious
- Pruning: sort the array and `break` early when `nums[i] > remaining` (avoid exploring dead branches)
- Pass `index i` (not `i+1`) to allow reuse of the same element
- Use `sub.copy()` when appending to results — lists are mutable!
- Time complexity is hard to nail precisely; mention O(2^(t/m)) or O(n^(t/m))

## 🎯 Common Use Cases

- Coin change problems (find all ways to make change)
- Recipe / ingredient combination problems
- Test case generation (combinations of inputs)
- Scheduling problems (all ways to fill a time slot)

## 🔗 Related Problems

- [Combination Sum II](../combination_sum_2/) — no element reuse, skip duplicates
- [Subsets](../subsets/) — all subsets without a target
- [Permutations](../permutations/) — ordered arrangements
- [Knapsack](../knapsack/) — select items within a weight/value budget
