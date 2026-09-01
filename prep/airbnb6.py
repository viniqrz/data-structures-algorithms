# Longest Subarray with Absolute Difference Limit (Sliding Window & Deque)

# Difficulty: Hard (Classic CodeSignal Q4).

# Problem: Given an array of integers nums and an integer limit, return the size of the longest contiguous subarray such that the absolute difference between any two elements in this subarray is less than or equal to limit.

# Longest Subarray with Absolute Difference Limit

# Input: nums = [10, 1, 2, 4, 7, 2], limit = 5

# Output: 4

# Explanation: The longest contiguous subarray where the absolute difference between any two elements is less than or equal to 5 is [2, 4, 7, 2]. The maximum element is 7 and the minimum is 2, yielding an absolute difference of exactly 5.


def solution(nums, limit):

    global_longest = 0
    
    for i in range(len(nums)):

        local_longest = 0
        arr = []

        for k in range(i+1, len(nums)):

              arr = nums[i:k+1]
             
              if abs(max(arr) - min(arr)) > limit:
                   break

              local_longest = len(arr)

        print(arr, local_longest, global_longest)
        global_longest = max(local_longest, global_longest)

    print(global_longest)

    return global_longest


solution([10, 1, 2, 4, 7, 2], 5)


