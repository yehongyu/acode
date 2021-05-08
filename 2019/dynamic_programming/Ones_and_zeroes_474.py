class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        nums = []
        for chs in strs:
            cnt1 = 0; cnt0 = 0
            for ch in chs:
                if ch == '1':
                    cnt1 += 1
                else: cnt0 += 1
            nums.append([cnt0, cnt1])
        dp = []
        for i in range(m+1): dp.append([0] * (n+1))
        res = 0
        for cnt0, cnt1 in nums:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i-cnt0>= 0 and j-cnt1>=0:
                        dp[i][j] = max(dp[i][j], dp[i-cnt0][j-cnt1]+1)
                    res = max(res, dp[i][j])
            print(cnt0, cnt1, dp)
        return res

s = Solution()
Array = ["10", "0001", "111001", "1", "0"]; m = 5; n = 3
print(s.findMaxForm(Array, m, n))
Array = ["10","0","1"]
m = 1
n = 1
