# Valid Palindrome

> A string is a palindrome if it reads the **same forwards and backwards**. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

Use **two pointers** — one from the left, one from the right — and march them inward, comparing characters at each step. If they ever differ, it's not a palindrome. If they meet in the middle, it is.

```
Algorithm:
  left, right = 0, len(s) - 1
  while left < right:
      if s[left] != s[right]: return False
      left += 1; right -= 1
  return True
```

## 📊 Visual

```
"r  a  c  e  c  a  r"
  L              R    → r == r ✓
     L        R       → a == a ✓
        L  R          → c == c ✓
           M          → (met in middle, odd length) → PALINDROME ✓

"a  n  n  a"
  L       R           → a == a ✓
     L  R             → n == n ✓
     R  L             → (pointers crossed) → PALINDROME ✓

"a  n  n  a  a"
  L         R         → a == a ✓
     L    R           → n == a ✗ → NOT PALINDROME ✗
```

## 📜 History & Background

Palindrome detection is one of the oldest string problems, with palindromes known since ancient Greek and Latin literature ("SATOR AREPO TENET OPERA ROTAS" — a famous Latin palindrome square). In CS it's a foundational problem for teaching two-pointer technique.

## 💼 Tech Interview Tips

- For **LeetCode 125** ("Valid Palindrome"): skip non-alphanumeric chars with `isalnum()` and `lower()`
- **Palindrome substrings** (LeetCode 5, 647): expand from centre approach — O(n²)
- Even-length palindromes have two centres; odd have one
- Two-pointer O(1) space is optimal; O(n) string reverse (`s == s[::-1]`) also works but uses extra space
- Follow-up: "minimum deletions to make palindrome" → DP (LCS variant)

## 🎯 Common Use Cases

- Input validation (palindrome words, numbers, dates like 02/02/2020)
- DNA sequence analysis (palindromic sequences recognised by restriction enzymes)
- Cryptography and coding theory
- String manipulation interview warm-up question

## 🔗 Related Problems

- [Is Anagram](../is_anagram/) — another character-level string check
- [Longest Common Subsequence](../longest_common_subsequence/) — DP on strings
- [Longest Substring](../longest_substring/) — sliding window on strings
