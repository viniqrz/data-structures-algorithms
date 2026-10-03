# Longest Substring Without Repeating Characters:
# Expand your right pointer to add characters to a hash set.
# If you encounter a duplicate, shrink the left pointer until the duplicate is gone.

def lss(text):

  l, r = 0, 0

  currSet = set()

  maxLen = 0

  while r < len(text) - 1:

    if text[r] in currSet:
      currSet.remove(text[l])
      l+=1
      continue

    currSet.add(text[r])
    maxLen = max(maxLen, len(currSet))
    print(currSet, len(currSet), text[r])
    r += 1

  return maxLen

print(lss('soekosekabcdfe'))