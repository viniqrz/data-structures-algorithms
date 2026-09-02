# Divisible Sum Pairs (Hash Map & Modular Arithmetic)

# Difficulty: Medium (Typical CodeSignal Q2).

# Problem: Given an array of integers a and an integer k,
# find the number of pairs (i, j) such that i < j and the sum a[i] + a[j] is divisible by k.

# Input: a = [1, 2, 3, 4, 5, 6], k = 5 Output: 3

# Explanation: The valid index pairs (i, j) are (0, 3) where $1 + 4 = 5$, (1, 2)
# where $2 + 3 = 5$, and (3, 5) where $4 + 6 = 10$.


def is_divisible_by(num, k):
    return num % k == 0

def solution(a, k):

    pairs = set()

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if not is_divisible_by(a[i] + a[j], k):
                continue

            pairs.add((i,j)) 

    print(pairs, len(pairs))

    return len(pairs)

solution([1, 2, 3, 4, 5, 6], 5)
