#coding=utf-8

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        n = len(A)
        if n <= 2:
            return -1
        start = 0; end = n - 1
        while start + 1 < end: # 这个条件可以避免出现死循环
            mid = start + (end-start)/2
            if A[mid-1] < A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] < A[mid] < A[mid+1]:
                start = mid
            elif A[mid-1] > A[mid] > A[mid+1]:
                end = mid
            else:
                end = mid
        if start > 0 and start < n and A[start-1] < A[start] > A[start+1]:
            return start
        if end > 0 and end < n and A[end-1] < A[end] > A[end+1]:
            return end
        return -1

s = Solution()
print(s.findPeak([1, 2, 1, 3, 4, 5, 7, 6]))
print(s.findPeak([1,2,3,4,1]))
