def bubbleSort(nums):

    n = len(nums)

    for i in range(n):
        for j in range (n - 1):
            if(nums[j] > nums[j + 1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums













nums = [3,1,6,5,7,2,9,8]
print(bubbleSort(nums))