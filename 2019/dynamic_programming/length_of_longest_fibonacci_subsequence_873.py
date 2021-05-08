class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = {}
        n = len(A)
        res = 0
        if n < 3: return 0
        dp[A[0]] = 1
        dp[A[1]] = 1
        for i in range(2, n):
            tmp = 1
            for j in range(i):
                if A[j]!=A[i]-A[j] and A[i]-A[j] in dp:
                    tmp = max(tmp, dp[min(A[j],A[i]-A[j])]+2)
                    print(A[i], A[j], A[i]-A[j], dp)
            dp[A[i]] = tmp
            res = max(res, dp[A[i]])
            print(i, A[i], dp[A[i]], res)
        return 0 if res < 3 else res

s = Solution()
A = [1,2,3,4,5,6,7,8]
A = [2,4,7,8,9,10,14,15,18,23,32,50]
A = [2,4,5,6,7,8,11,13,14,15,21,22,34]
print(s.lenLongestFibSubseq(A))