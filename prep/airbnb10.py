# Prefix String Concatenation (String Manipulation & Array Iteration)

# Difficulty: Easy (Typical CodeSignal Q1).

# Problem: Given an array of strings words and a target string s, determine if s is a prefix string of words. A string s is considered a prefix string if it can be formed by concatenating the first k strings in words (where k is between 1 and the length of words).

# Input: words = ["i", "love", "eating", "burger"], s = "iloveeating"
# Output: True

# Explanation: The target string s can be formed by concatenating the first 3 strings of the array ("i" + "love" + "eating").

def solution(words, s):

  is_prefix = True

  prefix = ''

  for i in range(len(words)):
    word_size = len(words[i])
    
    substr_s = s[len(prefix) : len(prefix) + word_size]

    print(substr_s, words[i], len(prefix) + word_size <= len(s))
    
    if substr_s != words[i]:
      if len(prefix) + word_size <= len(s) or (len(substr_s) != words[i] and len(prefix) < len(s)):
        is_prefix = False
  
    prefix += words[i]
    
  print(is_prefix)

  return is_prefix
  
solution(["i", "love", "eatingd", "burger"], 'iloveeating')