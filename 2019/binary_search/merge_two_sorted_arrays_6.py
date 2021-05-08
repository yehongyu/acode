#coding=utf-8

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        if m == 0:
            return B[0:]
        if n == 0:
            return A[0:]
        res = []
        i = 0; j = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        if i < m:
            res.extend(A[i:m])
        if j < n:
            res.extend(B[j:n])
        return res

s = Solution()
print(s.mergeSortedArray([1], [1]))
print(s.mergeSortedArray([1, 2, 3, 4], [2, 4, 5, 6]))
