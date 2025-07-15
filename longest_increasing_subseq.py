# Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

def solution(nums):
    maxLen = 0
    cache = {}
    
    def dfs(prev, curr, seq):
        if curr >= len(nums):
            return 0
        
        if (prev,curr) in cache:
            return cache[(prev,curr)]
        
        res = 0
        
        if nums[curr] > nums[prev]:
           res = 1 + dfs(curr, curr+1, seq)
        else:
           res = dfs(prev, curr+1)
       
        cache[(prev,curr)] = res

        return res

    for i in range(len(nums)):
        res = 1 + dfs(i, i+1)
        maxLen = max(maxLen, res)

    return maxLen


# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

print(solution([10,9,2,5,3,7,101,18]))

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

print(solution([0,1,0,3,2,3]))

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

print(solution([7,7,7,7,7,7,7]))
