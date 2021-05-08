class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n <= 2: return 0
        res = 0; i = 0
        while i < n:
            j = i
            while j+1 < n and A[j] < A[j+1]:
                j += 1
            if j == i:
                i = i+1; continue
            k = j
            while k+1 < n and A[k] > A[k+1]:
                k += 1
            if k == j:
                i = k; continue
            res = max(res, k-i+1)
            i = k
        return res



s = Solution()
nums = [2,1,4,7,3,2,5]
nums = [2,2,2]
print(s.longestMountain(nums))
