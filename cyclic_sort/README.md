# Cyclic Sort

> Sort an array of integers in range **1..n** in O(n) time and O(1) space. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

If numbers are in the range 1 to n, each number **belongs at index `num - 1`**. Walk through the array: if the current number isn't at its correct index, **swap it there**. Repeat until everything is in place. Each number is swapped at most once → O(n) total.

```
Algorithm:
  for i in range(len(nums)):
      correct_idx = nums[i] - 1
      while nums[i] != nums[correct_idx]:   # keep swapping until placed
          swap(nums, i, correct_idx)
          correct_idx = nums[i] - 1
```

## 📊 Visual

```
Input: [3, 1, 5, 4, 2]  (range 1–5)

i=0: nums[0]=3, correct_idx=2 → swap → [5, 1, 3, 4, 2]
i=0: nums[0]=5, correct_idx=4 → swap → [2, 1, 3, 4, 5]
i=0: nums[0]=2, correct_idx=1 → swap → [1, 2, 3, 4, 5]
i=0: nums[0]=1 ✓ (1 == correct_idx 0+1)
i=1: nums[1]=2 ✓
i=2: nums[2]=3 ✓
...
Result: [1, 2, 3, 4, 5]  ✓
```

## 📜 History & Background

Cyclic sort is a variation of the **cycle detection** idea applied to permutations. It's not widely attributed to a single inventor but is a well-known technique for the class of "numbers 1 to n" problems — widely taught in competitive programming.

## 💼 Tech Interview Tips

- Only works when numbers are in a **known range** (e.g., 1 to n or 0 to n)
- After cyclic sort: walk the array again to find the index where `nums[i] != i+1` → that's the **missing number**
- Handles duplicates carefully: if `nums[i] == nums[correct_idx]`, skip (avoid infinite loop)
- Common follow-ups: find missing number, find duplicate, find all missing numbers

## 🎯 Common Use Cases

- Find the missing number in 1..n (LeetCode 268)
- Find the duplicate number (LeetCode 287)
- Find all missing/duplicate numbers in range
- In-place array sorting when range is known

## 🔗 Related Problems

- [Dutch National Flag](../dutch_national_flag/) — another O(n) in-place sort
- [Sort Colors](../sort_colors/) — sort 0s, 1s, 2s
