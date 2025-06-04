

def binary_search(list,target):
    left, right = 0, len(list) - 1
    
    while left <= right:
        ## right + left, not right - left!!!!!!!
        mid = (right + left ) // 2
        
        curr = list[mid]

        if target == curr:
            return mid
    
        if target > curr:
            left = mid+1
        else:
            right = mid-1
            
        
            


list = [1,2,3,4,5,6,7,8,9,10]

target = 9

print(binary_search(list, target))