

def combination_sum(nums, target):
    res, sub = [], []
    
    def backtrack(i, total):
        if total == target:
            res.append(sub.copy())
            return
        
        if total > target or i >= len(nums):
            return
        
        sub.append(nums[i])
        backtrack(i, total + nums[i])
        sub.pop()
        backtrack(i+1, total)
    
    backtrack(0,0)
        
    return res

list = [2, 3, 6, 7]

print(combination_sum(list, 7))