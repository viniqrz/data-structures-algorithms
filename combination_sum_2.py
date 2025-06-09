

def combination_sum(nums, target):
    res, sub = [], []
    
    nums.sort()
    
    def backtrack(i, total):
        if total == target:
            if sub not in res:
                res.append(sub.copy())
            return
        
        if total > target or i >= len(nums):
            return
        
        sub.append(nums[i])
        backtrack(i+1, total + nums[i])
        sub.pop()
        backtrack(i+1, total)
    
    backtrack(0,0)
        
    return res

list = [10,1,2,7,6,1,5]
target = 8

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

print(combination_sum(list, target))