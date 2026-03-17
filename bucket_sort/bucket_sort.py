def topKFrequent(nums, k):
    bucket = [None] * (len(nums) + 1)
    frequency_map = {}
    
    for n in nums:
        frequency_map[n] = frequency_map.get(n, 0) + 1
    
    for key in frequency_map:
        frequency = frequency_map[key]
        if bucket[frequency] is None:
            bucket[frequency] = []
        bucket[frequency].append(key)
    
    res = []
    
    for pos in range(len(bucket) - 1, -1, -1):
        if bucket[pos] is not None and len(res) < k:
            res.extend(bucket[pos])
    
    return res

print(topKFrequent([1,2,3,4,5,6,6,6,7,7,7,1], 3))
