# Sort Colors — Counting Sort

> Sort an array containing only 0s, 1s, and 2s using counting. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

Count the occurrences of 0, 1, and 2 in a first pass. Then overwrite the array in a second pass using those counts. Two passes, O(n) total.

```
Algorithm:
  count = [0, 0, 0]
  for x in nums: count[x] += 1

  idx = 0
  for color in range(3):
      for _ in range(count[color]):
          nums[idx] = color; idx += 1
```

> 💡 For the optimal **one-pass** solution, see [Dutch National Flag](../dutch_national_flag/).

## 📊 Visual

```
Input: [2, 0, 2, 1, 1, 0]

Pass 1 (count):
  count[0] = 2  (two 0s)
  count[1] = 2  (two 1s)
  count[2] = 2  (two 2s)

Pass 2 (rebuild):
  write 0 × 2: [0, 0, _, _, _, _]
  write 1 × 2: [0, 0, 1, 1, _, _]
  write 2 × 2: [0, 0, 1, 1, 2, 2]

Result: [0, 0, 1, 1, 2, 2] ✓
```

## 📜 History & Background

This is a specific application of **counting sort** (Seward, 1954), a non-comparison sort that achieves O(n) by exploiting a known range of values. **LeetCode 75** — "Sort Colors" — is the standard problem, often solved with either this two-pass approach or the optimal one-pass Dutch National Flag algorithm.

## 💼 Tech Interview Tips

- This two-pass counting approach is simple to explain and implement
- The optimal O(n) one-pass solution is the Dutch National Flag algorithm (three pointers)
- Interviewers often expect the one-pass solution as a follow-up
- Key insight of counting sort: works in O(n) because values are in a **known, small range**
- Don't sort by comparison when you know the value range — use counting sort!

## 🎯 Common Use Cases

- Sorting elements from a small, known set of categories
- Priority queue where priorities are a small integer set
- Histogram normalisation
- Counting sort as a subroutine in radix sort

## 🔗 Related Problems

- [Dutch National Flag](../dutch_national_flag/) — one-pass three-pointer solution to the same problem
- [Cyclic Sort](../cyclic_sort/) — O(n) sort for 1..n range
- [Bucket Sort](../bucket_sort/) — frequency-based bucketing
