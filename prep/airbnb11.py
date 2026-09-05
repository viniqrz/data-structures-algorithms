# Max Consecutive Replacements (Sliding Window)

# Difficulty: Medium/Hard (Typical CodeSignal Q3/Q4).

# Problem: Given a binary array nums (containing only 0s and 1s) and an integer k, return the maximum number of consecutive 1s you can achieve in the array by flipping at most k 0s to 1s.

# Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2

# Output: 6

# Explanation: By flipping the 0s at indices 4 and 5 (or 5 and 10), you can create a contiguous subarray of six 1s: [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0].


def solution(nums, k):
  
  max_len = 0
  curr_len = 0
  flip_count = 0
  
  for i in range(len(nums)):
    #  print(curr_len, max_len)
     
     if nums[i] == 1:
       curr_len += 1
       continue
    
     if nums[i] == 0:
       
       if flip_count == k:
         curr_len = 1
         flip_count = 1
       else:
        flip_count += 1
        curr_len += 1

     max_len = max(max_len, curr_len)
       
      #  print(curr_len)
  
  # print(max_len)	
  
  return max_len

solution([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)

solution([0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0], 2)

def solution2(nums, k):
  def dfs(i, flip_count, in_seq):
    if i == len(nums):
      return 0

    if nums[i] == 0 and flip_count == k:
      return 0

    options = []

    # SKIP?
    if not in_seq:
      options.append(dfs(i + 1, 0, False))

    if nums[i] == 0:
      options.append(1 + dfs(i + 1, flip_count + 1, True))
    else:
      options.append(1 + dfs(i + 1, flip_count, True))

    return max(options)

  return dfs(0, 0, False)


print(solution2([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))

print(solution2([0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0], 2))

