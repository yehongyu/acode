class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n <= 0: return 0
        if n == 1: return A[0]
        mn =cur_mn= A[0]; mx =cur_mx= A[0]
        total = A[0]
        for i in range(1, n):
            cur_mn = min(cur_mn+A[i], A[i])
            mn = min(mn, cur_mn)
            cur_mx = max(cur_mx+A[i], A[i])
            mx = max(mx, cur_mx)
            total += A[i]
        if mn == total: return mx
        else: return max(mx, total-mn)

s = Solution()
print(s.maxSubarraySumCircular(
    [-2,-3,-1]
))
