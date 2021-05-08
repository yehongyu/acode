#coding=utf-8

class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        # write your code here
        n = len(A)
        if n == 0:
            return False
        if n == 1:
            return target == A[0]
        start = 0
        end = n - 1
        while start + 1 < end:
            mid = start + (end-start)/2
            if A[mid] == target:
                return True
            if A[mid] > A[end]:
                if target >= A[start] and A[mid] > target:
                    end = mid
                else:
                    start = mid
            elif A[mid] < A[end]:
                if target <= A[end] and A[mid] < target:
                    start = mid
                else:
                    end = mid
            else:
                end -= 1
        if A[start] == target or A[end] == target:
            return True
        return False

s = Solution()
print(s.search([2,5,6,0,0,1,2], 0))
print(s.search([2,5,6,0,0,1,2], 3))
print(s.search([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 1))
print(s.search([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 0))
