class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        n = len(A)
        if n == 0: return res
        for i in range(n):
            cur_min = A[i]
            for j in range(i, n):
                cur_min = min(cur_min, A[j])
                res += cur_min
        return res

s = Solution()
print(s.sumSubarrayMins([3,1,2,4]))
