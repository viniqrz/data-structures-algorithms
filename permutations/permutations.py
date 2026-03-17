

def permutations(nums):
    n = len(nums)
    perm, ans = [], []
    
    def backtrack():
        if len(perm) >= n:
            ans.append(perm.copy())
            return
        
        for x in nums:
            if x not in perm:
                perm.append(x)
                backtrack()
                perm.pop()
    
    backtrack()
    
    return ans

list1 = [1,2,3,4,5]

print(len(permutations(list1)))