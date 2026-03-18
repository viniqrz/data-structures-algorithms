# Longest Common Subsequence (LCS)

> Find the longest sequence of characters that appears **in order** in both strings (not necessarily contiguous). &nbsp;⏱ Time `O(m·n)` &nbsp;💾 Space `O(m·n)`

## 🧠 The Idea

Use **memoised recursion** (or bottom-up DP). At each position `(i, j)`, if characters match, `1 + lcs(i+1, j+1)`; otherwise take the best of `lcs(i+1, j)` or `lcs(i, j+1)` (skip from either string).

```
recursive(i, j):
  if i >= len(s1) or j >= len(s2): return 0
  if s1[i] == s2[j]: return 1 + recursive(i+1, j+1)
  return max(recursive(i+1, j), recursive(i, j+1))
```

## 📊 Visual

```
s1 = "abcde",  s2 = "ace"

DP table (s2 as rows, s1 as cols):
       ""  a  b  c  d  e
    ""  0  0  0  0  0  0
    a   0  1  1  1  1  1
    c   0  1  1  2  2  2
    e   0  1  1  2  2  3  ← answer = 3

LCS = "ace" (positions 0,2,4 in s1; 0,1,2 in s2) ✓
```

## 📜 History & Background

LCS was formally studied in the **1970s** and is the foundation of **diff** tools (Unix `diff`, `git diff`). The O(m·n) DP algorithm was published by Wagner and Fischer (1974) and variations power modern version control systems, DNA alignment tools, and file comparison utilities.

## 💼 Tech Interview Tips

- LCS ≠ LCS**T** (Longest Common Sub**string** — contiguous). LCS allows gaps; substring does not
- Bottom-up DP is more interview-friendly than memoised recursion (no stack overflow risk)
- Space can be optimised to O(min(m,n)) using two rolling rows
- **Edit distance** (Levenshtein) is closely related — uses a similar DP table
- LeetCode 1143

## 🎯 Common Use Cases

- `git diff` and text comparison tools
- DNA / protein sequence alignment (bioinformatics)
- Plagiarism detection
- File synchronisation (rsync)
- Spell correction (edit distance)

## 🔗 Related Problems

- [Longest Increasing Subsequence](../longest_increasing_subsequence/) — LIS of one array
- [Longest Substring](../longest_substring/) — contiguous, no two strings
- [Is Palindrome](../is_palindrome/) — string property check
- [Knapsack](../knapsack/) — 2D DP pattern
