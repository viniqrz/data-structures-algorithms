# Vowel Consonant Pattern Match (String Matching)

# Difficulty: Easy/Medium (Typical CodeSignal Q2). Problem:

# Given a pattern (a string of 0s and 1s) and a source string of lowercase letters, count the number of substrings in source that match the pattern's length where 0 represents a vowel (a, e, i, o, u, y) and 1 represents a consonant.

# Example: For pattern = "010" and source = "amazing", the output is 2

# 0 = vowel
# 1 = consonant  "amazing" => "0101011" + ("010") => 2


# SOLUTION

# 1) convert word input into 0s and 1s format
# 2) then we can compare these two while sequentially iterating word string
# 3) we must also be able to distinct a vowel from a consonant, which we can do easily creating a hard-coded vowel list and checking against it

# EDGE CASES (must ask in interview before impl.)

# 1) what if word has a char. that is not a consonant or a vowel?

def solution(pattern, word):
  
  vowels = set(['a', 'e', 'i', 'o', 'u'])
  
  encoded_word = ''
  
  for i in range(len(word)):
    encoded_word += '0' if word[i] in vowels else '1'

  occurrences = 0
  
  for i in range(len(encoded_word)):
    not_found = False
    
    for k in range(len(pattern)):
      letter_word = encoded_word[i + k]
      letter_pattern = pattern[k]

      if letter_word != letter_pattern:
        
        not_found = True
        break
        
    if not_found:
      continue
    
    occurrences += 1
    
  return occurrences


# "amazing" => "0101011" + ("010") => 2


solution('010', 'amazing')

          
# No more than 15 minutes is expected on this

# Tip: use Set() for O(1) lookup on arrays/strings
    
    
  
