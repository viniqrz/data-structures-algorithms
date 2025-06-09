

def permutations(nums):
    n = len(nums)
    sol, ans = [], []
    
    def backtrack():
        if len(sol) >= n:
            ans.append(sol.copy())
            return
        
        for x in nums:
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()
                
    backtrack()
    
    return ans

list1 = [1,2,3,4,5]

print(len(permutations(list1)))