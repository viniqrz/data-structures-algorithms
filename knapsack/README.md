# 0/1 Knapsack Problem

> Maximise value of items in a bag without exceeding weight capacity. &nbsp;⏱ Time `O(n·W)` &nbsp;💾 Space `O(n·W)` · Brute Force `O(2^n)`

## 🧠 The Idea

For each item, you have a binary choice: **include** it (add its value, reduce remaining capacity) or **exclude** it (skip to next item). Use dynamic programming to cache subproblem results and avoid exponential recomputation.

```
DP recurrence:
  dp[i][w] = max value using first i items with capacity w

  if weights[i-1] > w:
      dp[i][w] = dp[i-1][w]          ← can't fit item i
  else:
      dp[i][w] = max(
          dp[i-1][w],                 ← exclude item i
          values[i-1] + dp[i-1][w - weights[i-1]]  ← include item i
      )
```

## 📊 Visual

```
Items: (value=300,w=2), (200,w=1), (400,w=5), (500,w=3)
Capacity W = 5

DP Table (rows=items, cols=capacity 0..5):
     0   1   2   3   4   5
  0  0   0   0   0   0   0
  1  0   0 300 300 300 300   ← item1 (val=300, w=2)
  2  0 200 300 500 500 500   ← item2 (val=200, w=1)
  3  0 200 300 500 500 500   ← item3 (val=400, w=5, too heavy for w<5)
  4  0 200 300 500 700 800   ← item4 (val=500, w=3)

Answer: dp[4][5] = 800
```

## 📜 History & Background

The knapsack problem was studied mathematically as early as **1897** (Mathews). **George Dantzig** described the fractional version in 1957. It's one of the 21 **NP-complete problems** identified by Karp (1972) in the 0/1 form, yet solvable in pseudo-polynomial time with DP.

## 💼 Tech Interview Tips

- **0/1 knapsack** = each item used at most once. **Unbounded** = items reusable (→ [Combination Sum](../combination_sum/))
- Can optimise space to O(W) with a **rolling 1D array** (iterate weights backwards to avoid using item twice)
- Recognise knapsack patterns: "select subset to maximise/minimise value within a constraint"
- LeetCode variants: Partition Equal Subset Sum (LC 416), Target Sum (LC 494), Coin Change (LC 322)

## 🎯 Common Use Cases

- Cargo/luggage loading optimisation
- Portfolio management (maximise return within budget)
- Resource allocation in cloud computing
- Feature selection in machine learning
- Project selection with budget constraints

## 🔗 Related Problems

- [Combination Sum](../combination_sum/) — unbounded knapsack variant
- [Subsets](../subsets/) — enumerate all possible selections
- [House Robber III](../house_robber_3/) — tree-based include/exclude DP
- [Longest Increasing Subsequence](../longest_increasing_subsequence/) — another classic DP
