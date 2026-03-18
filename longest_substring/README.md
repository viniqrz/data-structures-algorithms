# Longest Substring Without Repeating Characters

> Find the length of the longest **substring** (contiguous) with all unique characters. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(min(n, m))` where m = charset size

## 🧠 The Idea

Use a **sliding window** with a set to track characters in the current window. Expand right to grow the window. When a duplicate is found at `r`, shrink from the left (`l++`) until the duplicate is removed. Track the maximum window size seen.

```
Algorithm:
  char_set = set()
  l = 0
  for r in range(len(s)):
      while s[r] in char_set:
          char_set.remove(s[l]); l += 1
      char_set.add(s[r])
      max_len = max(max_len, r - l + 1)
```

## 📊 Visual

```
s = "abcabcbb"

r=0: window="a"      set={a}       len=1
r=1: window="ab"     set={a,b}     len=2
r=2: window="abc"    set={a,b,c}   len=3  ← current max
r=3: s[3]='a' in set → remove s[l]='a', l=1
     window="bca"    set={b,c,a}   len=3
r=4: s[4]='b' in set → remove s[l]='b', l=2
     window="cab"    set={c,a,b}   len=3
r=5: s[5]='c' in set → shrink → window="abc"... len=3
r=6: s[6]='b' in set → shrink → window="cb" len=2
r=7: s[7]='b' in set → shrink → window="b" len=1

Answer: 3 ("abc") ✓
```

## 📜 History & Background

This is **LeetCode 3** — one of the most popular medium problems and a go-to introduction to the **sliding window** technique. It demonstrates how to maintain a constraint over a dynamic window in linear time.

## 💼 Tech Interview Tips

- Using a **dict** (char → last index) instead of set allows `l = max(l, dict[s[r]] + 1)` — O(1) jump instead of shrinking loop by loop
- Window size formula: `r - l + 1`
- The set/dict only tracks the **current window**, not all characters seen
- Variations: at most K distinct characters (LeetCode 340), at most 2 distinct (LeetCode 159)
- Edge cases: empty string → 0; all same characters → 1

## 🎯 Common Use Cases

- Network packet deduplication windows
- Text compression pre-processing
- Streaming data deduplication
- Finding unique segments in genomic sequences

## 🔗 Related Problems

- [Character Replacement](../character_replacement/) — sliding window with K replacements allowed
- [Longest Common Subsequence](../longest_common_subsequence/) — non-contiguous version
- [Is Anagram](../is_anagram/) — character frequency comparison
