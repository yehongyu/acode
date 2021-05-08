
'''
    
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
If target is found in the array return its index, otherwise, return -1.

l,r

if target == arr[mid]:
    return mid
if arr[l] <= target:
    if target < arr[mid]:
        r = mid - 1
    else:
        l = mid + 1
else:
    if acc[mid] < target:
        l = mid + 1
    else: 
        r = mid - 1


'''

def func(arr, target):
    size = len(arr)
    if size == 0: return -1
    l = 0; r = size-1
    while l <= r:
        mid = l + (r-l)//2
        if target == arr[mid]:
            return mid
        if arr[l] <= arr[mid]:
            if arr[l] <= target < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if arr[mid] < target < arr[l]:
                l = mid + 1
            else: 
                r = mid - 1
    return -1

nums = [4,5,6,7,0,1,2,3]
target = 0
res = func(nums, target)
print(res)




