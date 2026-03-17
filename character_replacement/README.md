# Longest Repeating Character Replacement — Sliding Window

> Longest substring where you can replace at most **K** characters to make all chars the same. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

Use a **sliding window**. A window is valid if `window_size - max_freq ≤ k` — meaning we can replace all non-dominant characters within budget k. When the window becomes invalid, slide the left pointer right. The max_freq never needs to decrease because we're looking for the maximum window.

```
Key insight:
  replacements_needed = window_length - count_of_most_frequent_char
  if replacements_needed > k → shrink window from left
```

## 📊 Visual

```
s = "AABAABABA",  k = 2

  A A B A A B A B A
  L R               window="A", max_freq=1, len-max=0 ≤ 2 ✓
  L   R             window="AAB", max_freq=2, 3-2=1 ≤ 2 ✓
  L     R           window="AABA", max_freq=3, 4-3=1 ≤ 2 ✓
  L       R         window="AABAA", max_freq=4, 5-4=1 ≤ 2 ✓
  L         R       window="AABAAB", max_freq=4, 6-4=2 ≤ 2 ✓
  L           R     window="AABAABA", 7-4=3 > 2 → shrink!
    L         R     window="ABAABA", ...

Result: 6
```

## 📜 History & Background

This is **LeetCode 424**, a classic sliding window problem. The elegant insight — that `max_freq` never needs to decrease — makes it a favourite interview question to test whether candidates truly understand the sliding window pattern.

## 💼 Tech Interview Tips

- The key trick: `max_freq` can only **increase** as we look for a longer valid window — never reset it
- Window constraint: `(right - left + 1) - max(freq.values()) > k`
- Space is effectively O(1) because there are only 26 uppercase letters
- Don't overcomplicate with frequency recalculations — stale `max_freq` is fine
- Variation: apply same pattern to binary strings (flip 0s to 1s)

## 🎯 Common Use Cases

- DNA / genomic sequence analysis
- String compression preprocessing
- Typewriter/autocorrect optimization
- Finding optimal character normalisation windows

## 🔗 Related Problems

- [Longest Substring](../longest_substring/) — sliding window without replacement
- [Subsets](../subsets/) — different exploration of string windows
