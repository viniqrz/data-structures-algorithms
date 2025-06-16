def characterReplacement(s: str, k: int) -> int:
    freqs = {}
    res = 0
    left = 0

    for right in range(len(s)):
        if freqs.get(s[right]):
            freqs[s[right]] += 1
        else:
            freqs[s[right]] = 1

        max_freq = max(freqs.values())
        curr_length = right - left + 1
        if curr_length - max_freq > k:
            freqs[s[left]] -= 1
            left += 1
            
        res = max(res, right-left+1)


    return res

print((characterReplacement('aabaababa', 2)))
