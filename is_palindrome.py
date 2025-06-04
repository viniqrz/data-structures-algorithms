from collections import Counter
from heapq import heapify, heappop, heappush


list = [10,9,5,1,2,3,4]
heapify(list)

print(heappop(list))

def is_palindrome(str:str):
    left, right = 0, len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
        
    return True

print(is_palindrome("ana"))
print(is_palindrome("annna"))
print(is_palindrome("anna"))
print(is_palindrome("annaa"))