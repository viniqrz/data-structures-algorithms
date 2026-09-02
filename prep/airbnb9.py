# Minesweeper Neighbor Count (2D m Traversal)

# Difficulty: Medium/Hard (Typical CodeSignal Q3).

# Problem: Given a 2D boolean matrix m where True represents a mine and False represents an empty cell, return a 2D integer m of the same dimensions where each cell contains the count of mines in its immediately adjacent neighbors (including diagonals).

# Input:

# Python

# m = [
#     [True, False, False],
#     [False, True, False],
#     [False, False, False]
# ]

# Output:

# Python
# [
#     [1, 2, 1],
#     [2, 1, 1],
#     [1, 1, 1]
# ]

# Explanation: The empty cell at (0, 1) is touching 2 mines (at (0, 0) and (1, 1)). The mine at (1, 1) is touching 1 mine at (0, 0).

import copy

def count_neighboring_bombs(i, j, m):
  has_left = j - 1 >= 0
  has_right =  j + 1 < len(m[i])
  has_top = i - 1 >= 0
  has_bottom =  i + 1 < len(m)

  count = 0

  if has_top and has_left and m[i-1][j-1]:
    count += 1

  if has_top and m[i-1][j]:
    count += 1

  if has_top and has_right and m[i-1][j+1]:
    count += 1

  if has_left and m[i][j-1]:
    count += 1

  if has_right and m[i][j+1]:
    count += 1

  if has_bottom and has_left and m[i+1][j-1]:
    count += 1

  if has_bottom and m[i+1][j]:
    count += 1

  if has_bottom and has_right and m[i+1][j+1]:
    count += 1

  return count

def solution(m):

    res = copy.deepcopy(m)

    for i in range(len(m)):
        for j in range(len(m)):

            res[i][j] = count_neighboring_bombs(i, j, m)

    print(res)

    return res

solution([
    [True, False, False],
    [False, True, False],
    [False, False, False]
])
            


            



            