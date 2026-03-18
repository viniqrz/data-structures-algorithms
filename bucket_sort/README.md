# Top K Frequent Elements — Bucket Sort

> Find the **K most frequent** elements in O(n) using bucket sort. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(n)`

## 🧠 The Idea

Instead of sorting by frequency (O(n log n)), use the **frequency itself as the bucket index**. An element can appear at most `n` times in an array of length `n`, so we only need `n+1` buckets. Fill the buckets, then read from the highest-frequency bucket down.

```
Algorithm:
  1. Count frequencies with a hash map
  2. Create buckets[0..n] where bucket[freq] = [elements with that freq]
  3. Iterate buckets from n down to 0, collect until we have K results
```

## 📊 Visual

```
nums = [1, 1, 1, 2, 2, 3],  k = 2

Frequency map: {1: 3, 2: 2, 3: 1}

Buckets (index = frequency):
  [0]  []
  [1]  [3]
  [2]  [2]
  [3]  [1]   ← highest

Read from top: [1] then [2] → answer: [1, 2] ✓
```

## 📜 History & Background

Bucket sort is a distribution sort dating back to early computer science. This specific "bucket by frequency" trick is a clever adaptation that achieves **linear time** for the top-K problem, beating the O(n log n) lower bound for comparison-based sorting.

## 💼 Tech Interview Tips

- The naive approach is `Counter(nums).most_common(k)` → O(n log n); this bucket solution is **O(n)**
- Bucket size must be `len(nums) + 1` (frequency range 0 to n inclusive)
- Alternative: use a **min-heap of size K** → O(n log k), good when K is much smaller than n
- Interviewers may ask to handle ties — bucket sort handles them naturally (all in same bucket)

## 🎯 Common Use Cases

- Analytics dashboards (top trending items)
- Recommendation engines (most viewed/purchased)
- Log analysis (most frequent errors)
- Text frequency analysis (most common words)

## 🔗 Related Problems

- [Heap](../heap/) — heap-based O(n log k) alternative
- [Sort Colors](../sort_colors/) — another counting-based sort
- [Is Anagram](../is_anagram/) — uses frequency counting
