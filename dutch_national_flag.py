def sortColors(nums):
    low, mid, high = 0, 0, len(nums)-1
    while mid <= high:
        if nums[mid] == 1:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


print(sortColors([1,1,1,2,2,2,2,2,1,1,2,2,3,3,3,3,2,2,3,3,3,3]))


def bruteForce(nums):
    array = [0, 0, 0]
    for i in range(len(nums)):
        array[nums[i]] += 1
    
    for i in range(len(nums)):
        if array[0] != 0:
            nums[i] = 0
            array[0] -= 1
        elif array[1] != 0:
            nums[i] = 1
            array[1] -= 1
        else:
            nums[i] = 2
    
    return nums

print(bruteForce([0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,2,2,2,2]))
