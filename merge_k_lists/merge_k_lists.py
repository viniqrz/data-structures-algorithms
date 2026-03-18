

def merge_lists(l1, l2):
    print(l1,l2)
    p1,p2 = 0,0
    ans = []
    while p1 < len(l1) or p2 < len(l2):

        if p1 >= len(l1):
            ans.append(l2[p2])
            p2+=1
            continue

        if p2 >= len(l2):
            ans.append(l1[p1])
            p1+=1
            continue
            
        
        if l1[p1] < l2[p2]:
            ans.append(l1[p1])
            p1+=1
        else:
            ans.append(l2[p2])
            p2+=1


    return ans


def mergeKLists(lists): 
    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:
        temp = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            if i + 1 >= len(lists):
                temp.append(l1)
                continue
            
            l2 = lists[i+1] if i + 1 < len(lists) else None
            temp.append(merge_lists(l1, l2))
        lists = temp
        
    return lists[0]


print([x for x in range(0, 10, 2)])
print(list(range(0, 20, 2)))

print(mergeKLists([[1,4,8],[0,2,5],[3,6,9]]))

