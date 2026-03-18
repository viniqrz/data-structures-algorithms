# Maximum Subarray — Kadane's Algorithm

> Find the contiguous subarray with the **largest sum**. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

At each position, decide: extend the current subarray, or start fresh from this element? If the running sum would make the current element worse than taking it alone, reset. Track the best sum seen globally.

```
Algorithm (Kadane's):
  cur_max, global_max = 0, -infinity
  for num in nums:
      cur_max = max(num, cur_max + num)   ← extend or restart
      global_max = max(global_max, cur_max)
  return global_max
```

## 📊 Visual

```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

  n    cur_max            global_max
 -2    max(-2, 0+(-2))=-2     -2
  1    max(1, -2+1)=1          1
 -3    max(-3, 1-3)=-2         1
  4    max(4, -2+4)=4          4
 -1    max(-1, 4-1)=3          4
  2    max(2, 3+2)=5           5
  1    max(1, 5+1)=6           6   ← MAX
 -5    max(-5, 6-5)=1          6
  4    max(4, 1+4)=5           6

Answer: 6  [4, -1, 2, 1] ✓
```

## 📜 History & Background

Published by **Joseph B. Kadane** of Carnegie Mellon University in 1984, after a challenge from Ulf Grenander. It was described by Jon Bentley in *Programming Pearls* (1986) as a beautiful example of algorithm design. It inspired many "sliding window maximum" variations.

## 💼 Tech Interview Tips

- Initialise `global_max = -infinity` (not 0!) to handle all-negative arrays
- `cur_max = 0` is fine as starting point — effectively means "no subarray yet"
- **Divide and conquer** alternative is O(n log n) but shows up in interviews as a "maximum crossing subarray" pattern
- Follow-up: return the **actual subarray** — track start/end indices when updating `global_max`
- LeetCode 53

## 🎯 Common Use Cases

- Maximum profit window in stock prices
- Best time period for a marketing campaign
- Signal processing (maximum energy segment)
- Financial analysis (best return period)
- Game score maximisation over a sequence

## 🔗 Related Problems

- [Knapsack](../knapsack/) — include/exclude DP pattern
- [Longest Increasing Subsequence](../longest_increasing_subsequence/) — DP on sequences
- [Longest Substring](../longest_substring/) — sliding window for strings
