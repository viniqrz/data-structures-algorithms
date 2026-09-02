# Alternating Sort (Two Pointers & Array Verification)

# Difficulty: Easy/Medium (Typical CodeSignal Q1/Q2).

# Problem: Given an array of integers a, construct a new array b by alternately taking elements from the beginning and the end of a (i.e., b[0] = a[0], b[1] = a[n-1], b[2] = a[1], b[3] = a[n-2], etc.). Return True if b is strictly increasing, and False otherwise.

# Input: a = [1, 3, 5, 6, 4, 2]

# Output: True

# Explanation: The constructed array b is [1, 2, 3, 4, 5, 6], which is strictly increasing.


def solution(a):

    # edge case 1
    if not len(a):
        return False
    
    is_increasing = True
    b = []

    l, r = 0, len(a) - 1

    while l < r:
        b.append(a[l])
        b.append(a[r])

        if a[l] >= a[r]:
            is_increasing = False

        l += 1
        r -= 1

    print(is_increasing, b)

    return is_increasing    


solution([1, 3, 5, 6, 4, 2])



