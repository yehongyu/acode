#coding=utf-8

class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        n = len(A)
        if n <= 0:
            return 0
        i = 0
        while i < len(A):
            if A[i] == elem:
                A.pop(i)
            else:
                i += 1
        return i

s = Solution()
print(s.removeElement([], 0))
print(s.removeElement([0, 4, 4, 0, 0, 2, 4, 4], 4))
