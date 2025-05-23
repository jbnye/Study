def mergeSort (nums):

    left = nums[:len(nums) // 2]
    right = nums[len(nums) // 2:]
    if(len(nums) <= 1):
        return

    mergeSort(left)
    mergeSort(right)

    i =0
    j =0
    k =0

    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            nums[k] = left[i]
            i += 1
            k += 1
        else:
            nums[k] = right[j]
            j += 1
            k +=1
        
    while(i < len(left)):
        nums[k] = left[i]
        i += 1
        k += 1
    while(j < len(right)):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums



nums = [3,1,6,5,7,2,9,8]
print(mergeSort(nums))












# def mergeSort (nums):
#     left = nums[:len(nums) // 2]
#     right = nums[len(nums) // 2 :]
#     if(len(nums) <= 1):
#         return nums
#     mergeSort(left)
#     mergeSort(right)

#     i = 0
#     j = 0
#     k = 0
#     while (i < len(left) and j < (len(right))):
#         if(left[i] < right[j]):
#             nums[k] = left[i]
#             i += 1
#         else:
#             nums[k] = right[j]
#             j += 1

#         k += 1

#     while i < len(left):
#         nums[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         nums[k] = right[j]
#         j += 1
#         k += 1

#     return nums

