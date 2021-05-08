#coding=utf-8

## 找到第一个大于等于target的数字的位置

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        n = len(A)
        if n <= 0:
            return 0
        start = 0
        end = n - 1
        if target < A[0]:
            return 0
        while start + 1 < end:
            mid = start + (end-start)/2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            return end
        if A[end] < target:
            return end + 1
        if A[start] == target:
            return start
        return start + 1

s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 0))

