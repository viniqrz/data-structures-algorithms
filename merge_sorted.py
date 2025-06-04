


def merge_sorted(sorted1,sorted2):
    s1, s2 = 0, 0
    
    res = []
    
    while s1 < len(sorted1) or s2 < len(sorted2):
        if (s1 >= len(sorted1)):
            res.append(sorted2[s2])
            s2 += 1
            continue
        if (s2 >= len(sorted2)):
            res.append(sorted1[s1])
            s1 += 1
            continue
        
        if sorted1[s1] < sorted2[s2]:
            res.append(sorted1[s1])
            s1 += 1
        else:
            res.append(sorted2[s2])
            s2 += 1
          
    return res  
    

sorted1 = [1,4,6,8]
sorted2 = [2,3,5,7]

print(merge_sorted(sorted1, sorted2))