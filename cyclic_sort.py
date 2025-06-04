

def cyclic_sort(list):
    
    def swap(list, i, j):
        list[j], list[i] = list[i], list[j]
        
    for i in range(len(list) - 1):
        
        correct_idx = list[i] - 1 
        
        if (list[i] != list[correct_idx]):
            swap(list, i, correct_idx)
            
    return list
    
    
list = [1,2,3,5,4,6,7,9,8,10]

print(cyclic_sort(list))