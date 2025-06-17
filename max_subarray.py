from math import inf


def maxSubArray(nums):
    cur_max, max_till_now = 0, -inf
    for c in nums:
        cur_max = max(c, cur_max + c)
        max_till_now = max(max_till_now, cur_max)
    return max_till_now

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Input: nums = [1]
# Output: 1

# Input: nums = [5,4,-1,7,8]
# Output: 23

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))
