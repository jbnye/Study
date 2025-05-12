

def binarySearch (arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    middle = 0
    while(left <= right):
        middle = (left + right) //2
        if(arr[middle] < target):
            left = middle +1
        elif(arr[middle] > target):
            right = middle - 1
        else:
            return True
    return False


nums = [3,6,1,4,3,2,7,9,2,11,34,5,4,23,54,32,0,431]
target = 11
ans = binarySearch(nums, target)
print(ans)




    # arr.sort()
    # left = 0
    # right = len(arr) - 1
    # middle = 0
    # while left <= right:
    #     middle = (left + right) // 2
    #     if(arr[middle] == target):
    #         return True
    #     elif(arr[middle] < target):
    #         left = middle + 1
    #     else:
    #         right = middle - 1

    # return False