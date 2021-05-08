class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        acc = [0]
        n = len(A)
        for i in range(len(A)):
            acc.append(acc[-1] + A[i])
        total = acc[-1]
        res = A[0]
        for i in range(1, n+1):
            for j in range(i):
                res = max(res, acc[i]-acc[j])
                if not (i==n and j== 0):
                    res = max(res, acc[j]-acc[i]+total)
                print(i, j, res, acc[i]-acc[j], acc[j]-acc[i]+total)
        return res

s = Solution()
print(s.maxSubarraySumCircular([-2,-3,-1]))