# Longest Increasing Subsequence (LIS)

> Find the length of the longest **strictly increasing** subsequence (elements don't need to be contiguous). &nbsp;⏱ Time `O(n²)` DP · `O(n log n)` patience sorting &nbsp;💾 Space `O(n)`

## 🧠 The Idea

**DP approach**: `dp[i]` = length of longest increasing subsequence ending at index `i`. For each `i`, look back at all `j < i` where `nums[j] < nums[i]` and take `max(dp[j]) + 1`.

```
dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i])
Answer = max(dp)
```

## 📊 Visual

```
nums = [10, 9, 2, 5, 3, 7, 101, 18]

Index:   0   1   2   3   4   5    6    7
Value:  10   9   2   5   3   7  101   18
dp:      1   1   1   2   2   3    4    4

LIS: [2, 3, 7, 101] or [2, 3, 7, 18] → length 4 ✓

Build dp[5]=3: nums[5]=7 > nums[2]=2(dp=1), nums[3]=5(dp=2), nums[4]=3(dp=2)
              → dp[5] = max(1,2,2) + 1 = 3
```

## 📜 History & Background

LIS has been studied since the 1960s. The O(n²) DP was well-known early on; the O(n log n) solution using **patience sorting** (a card game strategy!) was developed by Schensted (1961) and later connected to **Dilworth's theorem** in combinatorics.

## 💼 Tech Interview Tips

- O(n²) DP is almost always acceptable in interviews — mention O(n log n) as a bonus
- O(n log n) trick: maintain a `tails` array where `tails[i]` = smallest tail of IS of length `i+1`, use binary search to find insert position
- Don't confuse with **Longest Common Subsequence** (two strings) or **Longest Consecutive Sequence** (no gaps allowed)
- The answer is `max(dp)`, not `dp[-1]` — the LIS might end anywhere
- LeetCode 300

## 🎯 Common Use Cases

- Version sequencing / changelog ordering
- Stack of boxes problem (can stack if all dimensions smaller)
- Russian dolls problem (LeetCode 354 — 2D LIS)
- Patience sorting algorithm
- Scheduling non-overlapping intervals (greedy + binary search)

## 🔗 Related Problems

- [Longest Common Subsequence](../longest_common_subsequence/) — LCS of two strings
- [Longest Consecutive Sequence](../longest_consecutive_sequence/) — consecutive integers
- [Knapsack](../knapsack/) — include/exclude DP pattern
