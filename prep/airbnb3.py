# Minimum Window Substring (Hash Table & Sliding Window)

# Difficulty: Hard (Frequent Airbnb Q3/Q4). Problem: Given two strings s and t, return the minimum window in s which contains all characters of t.  

# Context: Hash-table problems represent roughly 31 percent of Airbnb's coding challenges, often hybridizing with strings and sliding window techniques like this specific problem.

# s = string
# t = string

# min window in s which contains all chars of t

# SOLUTION

# 1) we can interate through t to create a set
# 2) then we can interate through s to look for matches in set
# 3) check match count, if it has size of set, if so, found a window
# 4) check if window size is smaller than smallest one so far, if so, replace it 

## example: s = 'abcdkjeskjkjs'

def solution(s, t):
   
    t_set = set(t)
    t_set_size = len(t_set)

    l, r = 0, t_set_size

    min_window = 10**30 # infinity

    while l < len(s) - t_set_size and r < len(s) + 1:
        window = s[l:r]
      
        window_set = set(window)
        curr_window_count = len(window)
        
        match = ""
        
        for window_char in window_set:
          if window_char in t_set:
            match += window_char

        if len(match) == t_set_size:
            print(window_set, t_set, curr_window_count, window)
            min_window = min(min_window, curr_window_count)
            l += 1
            r = l + t_set_size

        r += 1
    
    print(min_window)
    
    return min_window


# Standard Scenario, input s="ADOBECODEBANC" and t="ABC", result="BANC", "ADOBEC" (len 6) is found first, but "BANC" (len 4) is the absolute minimum.

solution('ADOBECODEBANC', 'ABC')




        

        
    
    
