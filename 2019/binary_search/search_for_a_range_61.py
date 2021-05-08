#coding=utf-8

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        n = len(A)
        if n <= 0:
            return [-1, -1]
        # find left bound
        start = 0
        end = n - 1
        while start + 1 < end:
            mid = start + (end-start)/2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            left = start
        elif A[end] == target:
            left = end
        else:
            left = -1
        # ding right bound
        start = 0
        end = n - 1
        while start + 1 < end:
            mid = start + (end-start)/2
            if A[mid] == target:
                start = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            right = end
        elif A[start] == target:
            right = start
        else:
            right = -1
        return [left, right]

s = Solution()
print(s.searchRange([], 9))
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))



