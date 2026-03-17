

# str1, str2

# e.g: abcd, adbc = abc
# recursive


#                     [a]bcd, [a]dbc OK
#          a[b]cd, [a]dbc FAIL ;  [a]bcd, a[d]bc OK
#          a[b]cd, [a]dbc FAIL ;  [a]bcd, a[d]bc OK
#          a[b]cd, [a]dbc FAIL ;  [a]bcd, a[d]bc OK
# a[b]cd, a[d]bc FAIL increase right index + 1
# a[b]cd, a[d]bc FAIL increase right index + 1
# a[b]cd, a[d]bc FAIL increase right index + 1
# a[b]cd, ad[b]c OK
# [a]bcd, [a]dbc


def solution(str1, str2):
    
    cache = {}
    
    def recursive(i, j):
        if i >= len(str1) or j >= len(str2):
            return 0
        
        if (i,j) in cache:
            return cache[(i,j)]
        
        left = recursive(i+1, j)
        right = recursive(i, j+1)
        
        seq = 0
        
        if str1[i] is str2[j]:
            seq = 1
        
        res = seq + max(left, right)

        cache[(i,j)] = res
       
        return res
    
    return recursive(0, 0)


# print(solution('abcd', 'adbc'))


# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
print(solution('abcde', 'ace'))


# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
print(solution('abc', 'abc'))


# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
print(solution('abc', 'def'))
