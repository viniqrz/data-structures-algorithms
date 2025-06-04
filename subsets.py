list = [1,2,3,4,5,6]

def subsets(list):
    res = []
    subset = []
    
    def dfs(i):
        if i >= len(list):
            res.append(subset.copy())
            return
        
        subset.append(list[i])
        dfs(i + 1)
        
        subset.pop()
        dfs(i + 1)

    dfs(0)
    
    return res

print(subsets(list))