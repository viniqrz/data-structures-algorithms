# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

def lcs(nums):
    nums = set(nums)
    count = 0

    for n in nums:
        if n - 1 not in nums:
            next = n + 1
            while next in nums:
                next += 1
            count = max(count, next - n)

    return count


print(lcs([100,4,200,1,3,2]))
print(lcs([0,3,7,2,5,8,4,6,0,1]))
print(lcs([1,0,1,2]))
