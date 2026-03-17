# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def longest_substr(s):
    sett = set()
    l = 0
    max_len = 0
    
    for r in range(len(s)):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
    
        sett.add(s[r])
        max_len = max(max_len, r-l+1)
 
    return max_len

  
print(longest_substr("abcabcbb"))
print(longest_substr("bbbbb"))
print(longest_substr("pwwkew"))
