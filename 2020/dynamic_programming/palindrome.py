class Solution(object):
    def get_palindrome_state(self, s):
        size = len(s)
        dp = []
        for i in range(size+1):
            dp.append([False] * (size+1))
            dp[i][i] = True
        for step in range(1, size):
            for i in range(0, size-step+1):
                if step == 1: dp[i][i+step] = True
                else:
                    if s[i] == s[i+step-1]:
                        dp[i][i+step] = dp[i+1][i+step-1]
        return dp

    def palindromePartition(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size <= 1: return 0
        palin_state = self.get_palindrome_state(s)
        print(palin_state)
        dp = [size+1] * (size+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(1, size+1):
            for j in range(0, i):
                if palin_state[j][i]:
                    dp[i] = min(dp[i], 1+dp[j])
        if dp[size] == size+1:
            return -1
        return dp[size]

    def longestIncreasingSubsequence(self,nums):
        size = len(nums)
        if size <= 1: return size
        dp = [1] * size
        for i in range(1, size):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return dp[size-1]

    def longestCommonSubsequence(self, a, b):
        m = len(a)
        n = len(b)
        if m <= 0 or n <= 0: return 0
        dp = []
        max_len = 0
        for i in range(m+1): dp.append([0] * (n+1))
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if a[i-1] == b[j-1]:
                    dp[i][j] = max(dp[i][j], 1+dp[i-1][j-1])
                max_len = max(max_len, dp[i][j])
        return max_len

    def longestCommonSubstring(self, a, b):
        m = len(a)
        n = len(b)
        if m <= 0 or n <= 0: return 0
        dp = []
        max_len = 0
        for i in range(m+1): dp.append([0] * (n+1))
        for i in range(1, m+1):
            for j in range(1, n+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = max(dp[i][j], 1+dp[i-1][j-1])
                max_len = max(max_len, dp[i][j])
        return max_len

if __name__ == "__main__":
    s = Solution()

    a = "abcbce"
    b = "cbdcdddde"
    res1 = s.longestCommonSubsequence(a, b)
    res2 = s.longestCommonSubstring(a, b)
    print("LCS, subsequence:", res1)
    print("LCS, substring:", res2)
    '''
    nums = [10,11,12,1,2,3,4,15]
    res = s.longestIncreasingSubsequence(nums)
    print("LIS:", res)
    
    aaa = "abcdc"
    res = s.get_palindrome_state(aaa)
    res = s.palindromePartition(aaa)
    print("palindrome:", res)
    '''
