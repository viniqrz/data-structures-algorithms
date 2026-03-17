# Combination Sum II — Backtracking (No Reuse)

> Find all **unique** combinations that sum to target — each element used **at most once**. &nbsp;⏱ Time `O(2^n)` &nbsp;💾 Space `O(n)`

## 🧠 The Idea

Like Combination Sum I, but: each element can only be used **once** (move to `i+1`), and the input may have **duplicates** that would produce duplicate results. Fix this by **sorting first**, then skipping duplicate elements at the same recursion level.

```
Key differences from Combination Sum I:
  - Call backtrack(i+1, ...)  instead of backtrack(i, ...)
  - Sort nums first
  - Skip duplicates: if i > start and nums[i] == nums[i-1]: continue
```

## 📊 Visual

```
nums = [1,1,2,5,6,7,10]  (sorted),  target = 8

Level 0: try each as first element
  Start with nums[0]=1:
    Start with nums[1]=1:  → [1,1,...] → finds [1,1,6]
    Start with nums[2]=2:  → [1,2,...] → finds [1,2,5]
    Start with nums[3]=5:  → [1,5,...] → no match (1+5+next > 8 or not found)
    ...
  Start with nums[1]=1: ← SKIP! same value as nums[0] at same level
  Start with nums[2]=2: → [2,...] → finds [2,6]
  ...
```

## 📜 History & Background

This is **LeetCode 40**. The duplicate-skipping trick is a fundamental pattern that appears in many backtracking problems involving non-distinct input arrays (e.g., Subsets II, Permutations II).

## 💼 Tech Interview Tips

- **Always sort first** when dealing with potential duplicates in backtracking
- Skip condition: `if i > start and nums[i] == nums[i-1]: continue` — `i > start` prevents skipping the *first* occurrence at a level
- Use `i+1` (not `i`) in the recursive call — no element reuse
- The sorting + skip pattern appears in: Subsets II, Permutations II, 3Sum, 4Sum
- Interviewers will probe: "what happens without the skip condition?" → duplicate combinations

## 🎯 Common Use Cases

- Lottery / raffle combination generation (no repeat draws)
- Unique portfolio allocations
- Finding unique ways to represent a value with distinct coins

## 🔗 Related Problems

- [Combination Sum](../combination_sum/) — allows element reuse
- [Subsets](../subsets/) — all subsets without target constraint
- [Permutations](../permutations/) — ordered arrangements
