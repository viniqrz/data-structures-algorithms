def sortColors(nums):
    array = [0, 0, 0]
    dictStack = {}

    for i in nums:
        if i in dictStack:
            dictStack[i] += 1
        else:
            dict
    
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

print(sortColors([0,0,0,1,1,1,2,1,1,1,1,1,1,2,2,2,2,1,1,2,2,2,2]))