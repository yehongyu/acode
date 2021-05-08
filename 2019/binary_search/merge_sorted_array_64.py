#coding=utf-8

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        if m == 0:
            for i in range(n):
                A[i] = B[i]
        if n == 0:
            return
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0 and k >= 0:
            if A[i] >= B[j]:
                A[k] = A[i]
                i -= 1; k -= 1
            else:
                A[k] = B[j]
                j -= 1; k -= 1
        if j >= 0:
            while j >= 0:
                A[k] = B[j]
                j -= 1; k -= 1



s = Solution()
'''
A = [1, 2, 3, None, None, None]
B = [4, 5]
m = 3; n = 2
s.mergeSortedArray(A, m, B, n)
print(A)
A = [1, 2, 5, None, None, None]
B = [3, 4]
m = 3; n = 2
s.mergeSortedArray(A, m, B, n)
print(A)
'''
A = [9,10,11,12,13, None, None, None, None]
m = 5
B = [4,5,6,7]
n = 4
s.mergeSortedArray(A, m, B, n)
print(A)
