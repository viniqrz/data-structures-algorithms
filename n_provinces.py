
def n_provinces(matrix: list):
    n = len(matrix)
    visited = [False]*n
    count = 0
    
    def dfs(city):
        for neighbor in range(n):
            if matrix[city][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor)

    for city in range(n):
        if not visited[city]:
            visited[city] = True
            count += 1
            dfs(city)

    return count

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
print(n_provinces([[1,1,0],[1,1,0],[0,0,1]]))

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
print(n_provinces([[1,0,0],[0,1,0],[0,0,1]]))
