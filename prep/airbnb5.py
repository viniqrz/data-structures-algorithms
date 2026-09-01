# Matrix Gravity Drop (2D Array Simulation)

# Difficulty: Medium/Hard (Classic CodeSignal Q3).

# Problem: You are given a 2D matrix of characters representing a grid where . is empty space, * is a solid obstacle, and # is a stone. Simulate gravity by letting all the stones # fall straight down until they hit the bottom of the grid, an obstacle *, or another stone. Return the resulting matrix.

# Input:

# Python
# matrix = [
#     ['.', '.', '.', '.', '#'],
#     ['#', '.', '#', '.', '.'],
#     ['.', '*', '.', '*', '.'],
#     ['#', '.', '#', '.', '#']
# ]

# Output:

# Python
# [
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['#', '*', '#', '*', '#'],
#     ['#', '.', '#', '.', '#']
# ]

# Explanation: The stones (#) in columns 0, 2, and 4 fall to the lowest available empty spaces (.) at the bottom of the grid. Obstacles (*) block stones from falling further.

# SOLUTION

# 1) gravity = moving index by index the '#' of towards the last index of first array OR until there's a '*' in the next index

def solution(matrix, n = 1):

    if n > len(matrix):
        return matrix

    def is_obstacle(val):
        return val == '*'
    
    def is_stone(val):
        return val == '#'

    def apply_gravity(matrix, i, k):

        if not is_stone(matrix[i][k]):
            return

        if is_obstacle(matrix[i+1][k]):
            return

        if is_stone(matrix[i+1][k]):
            return

        matrix[i][k], matrix[i+1][k] = '.', '#'

    for i in range(len(matrix) - 1):
        for k in range(len(matrix[i])):
            apply_gravity(matrix, i, k)

            
    return solution(matrix, n + 1)


matrix = [
    ['.', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '.'],
    ['.', '*', '.', '*', '.'],
    ['#', '.', '#', '.', '#']
]

# Find the maximum width needed for any item in the matrix
col_width = max(len(str(item)) for row in matrix for item in row)

# Print each row with aligned columns
for row in matrix:
    print(" ".join(f"{item:>{col_width}}" for item in row))

solution(matrix)

# print(matrix)

# Find the maximum width needed for any item in the matrix
col_width = max(len(str(item)) for row in matrix for item in row)

# Print each row with aligned columns
for row in matrix:
    print(" ".join(f"{item:>{col_width}}" for item in row))










