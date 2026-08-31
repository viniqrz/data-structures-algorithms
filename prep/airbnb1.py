# Problem: 

# Given an array a, return an array b of the same length where for each i:

# b[i] = a[i - 1] + a[i] + a[i + 1].

# If an index is out of bounds, use $0$ for that term.

# Example: For a = [4, 0, 1, -2, 3], the output is [4, 5, -1, 2, 1]. 


def solution(a):
  
  b = len(a) * [0]
  
  for i in range(len(a)):
    x = 0;
    y = 0;
    z = 0;
    
    if i - 1 >= 0:
       x = a[i - 1]
       
    y = a[i]
    
    if i + 1 < len(a):
       z = a[i + 1]	
    
    total = x + y + z
    b[i] = total
  
  return b

# it's expected that i finish this in less than 2-3 minutes, i shouldn't spend a lot of time, it's the simplest problem

solution([4, 0, 1, -2, 3])


# technique to solve sequential sliding window fast:

def solution(a):
    return [sum(a[max(0, i-1):i+2]) for i in range(len(a))]
    
# a[ max(0, i-1) : i+2 ]





