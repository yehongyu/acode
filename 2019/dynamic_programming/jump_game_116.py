import sys
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump_DP(self, A):
        # write your code here
        m = len(A)
        if m <= 1:
            return True
        dp = [False] * m
        dp[0] = True
        for i in range(1, m):
            for j in range(0, i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
        return dp[m-1]

    def jump_DP(self, A):
        m = len(A)
        if m <= 1:
            return 0
        dp = [sys.maxsize] * m
        dp[0] = 0
        pre = [-1] * m
        for i in range(1, m):
            for j in range(0, i):
                if dp[j] != sys.maxsize and j + A[j] >= i:
                    dp[i] = dp[j] + 1
                    pre[i] = j
                    break
        if dp[m-1] == sys.maxsize:
            return -1
        i = m - 1
        path = []
        while i >= 0:
            path.append(i)
            i = pre[i]
        path.reverse()
        print(path)
        return dp[m - 1]

    def jump_Greedy(self, A):
        m = len(A)
        if m <= 1:
            return 0
        res = 0; cur = 0; i = 0;
        while cur < m - 1:
            res += 1
            pre = cur
            while i <= pre:
                cur = max(cur, i + A[i])
                i += 1
            if pre == cur: return -1
        return res




s = Solution()
A = [3,2,1,0,4]
A = [13,52,42,21,58]
A = [2,3,1,1,4]
#print(s.jump_Greedy(A))
print(s.jump_DP(A))
