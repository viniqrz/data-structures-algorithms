

grid = [
    [0,1,2,3,4,5],
    [6,7,8,9,10,11],
    [12,13,14,15,16,17],
    [18,19,20,21,22,23],
]

def grid_dfs(grid):
    height, width = len(grid), len(grid[0])
    
    visited = set()
    
    def dfs(i, j):
        if i < 0 or i >= height or j < 0 or j >= width:
            return
        
        if (i,j) in visited:
            return
        
        visited.add((i,j))
        
        print(grid[i][j])
        
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        
    dfs(0, 0)
    
from collections import deque
    
def grid_bfs(grid):
    height, width = len(grid), len(grid[0])
    
    visited = set()
    
    queue = deque([(0,0)])
    
    while queue:
        i,j = queue.popleft()
        
        if i < 0 or i >= height or j < 0 or j >= width:
            continue
        
        if (i,j) in visited:
            continue
        
        visited.add((i,j))
        
        print(grid[i][j])
        
        queue.append((i+1,j))
        queue.append((i,j+1))
    
    
# print(grid_dfs(grid))
print(grid_bfs(grid))
        
        
        