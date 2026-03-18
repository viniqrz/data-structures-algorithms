# Valid Anagram

> Check if two strings are anagrams — same characters, same counts, different order. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

Two strings are anagrams if and only if they have the **same character frequency distribution**. The simplest check: count characters in both strings and compare. Python's `Counter` makes this a one-liner.

```
Options:
  1. Counter(s1) == Counter(s2)           → O(n), O(1) space (26 letters)
  2. sorted(s1) == sorted(s2)             → O(n log n) — easier but slower
  3. Build freq dict manually             → most explicit, O(n)
```

## 📊 Visual

```
"anagram" vs "nagaram":

a:3  n:1  g:1  r:1  m:1       a:3  n:1  g:1  r:1  m:1
        ↓                              ↓
      Counter = Counter  →  IS ANAGRAM ✓

"hello" vs "world":

h:1  e:1  l:2  o:1             w:1  o:2  r:1  l:1  d:1
     ↓                              ↓
   Counter ≠ Counter  →  NOT ANAGRAM ✗
```

## 📜 History & Background

Anagram detection is a classic string problem dating to early text processing. The word "anagram" itself comes from Greek (ana = back, gramma = letter). In competitive programming, the Counter/sort approach is standard; in production, normalised frequency arrays (size 26) are common for performance.

## 💼 Tech Interview Tips

- `Counter(s) == Counter(t)` is clean but import-dependent — know how to do it manually
- For **Unicode** strings: use a defaultdict (26-letter array only works for lowercase ASCII)
- Edge cases: different lengths → immediately `False`; empty strings → `True` (both are empty)
- Follow-up: "Group anagrams together" (LeetCode 49) — use `tuple(sorted(word))` as dict key
- `sorted` approach is O(n log n) but totally fine to mention as an alternative

## 🎯 Common Use Cases

- Spell checkers and word games (Scrabble, Wordle)
- Grouping anagrams in a word list
- Detecting plagiarism / text reshuffling
- Cryptographic transposition cipher analysis
- DNA pattern matching (finding rearrangements)

## 🔗 Related Problems

- [Is Palindrome](../is_palindrome/) — another character-level string check
- [Longest Substring](../longest_substring/) — sliding window over character sets
- [Character Replacement](../character_replacement/) — frequency counting in windows
