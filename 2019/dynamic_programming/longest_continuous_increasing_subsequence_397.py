class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence_old(self, A):
        # write your code here
        n = len(A)
        if n <= 2: return n
        dp = [2] * n
        res = 2
        for i in range(2, n):
            if A[i] > A[i-1] > A[i-2] or A[i] < A[i-1] < A[i-2]:
                dp[i] = dp[i-1] + 1
            res = max(res, dp[i])
        return res

    def findNumberOfLIS_OLD(self, nums):
        n = len(nums)
        if n <= 1: return n
        dp = [1] * n
        count = [1] * n
        max_len = 1
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                max_len = max(max_len, dp[i])
        print(dp)
        print(count)
        res = 0
        for i in range(n):
            if dp[i] == max_len:
                res += count[i]
        return res

    def longestIncreasingSubsequence(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        dp = [1] * n
        max_len = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                max_len = max(max_len, dp[i])
        return max_len

    def longestConsecutive(self, nums):
        n = len(nums)
        if n <= 1: return n
        visit = set()
        max_len = 1
        for i in range(n):
            if nums[i] in visit: continue
            visit.add(nums[i])
            left = nums[i] - 1
            while left in nums:
                visit.add(left)
                left -= 1
            right = nums[i] + 1
            while right in nums:
                visit.add(right)
                right += 1
            max_len = max(max_len, right-left-1)
        return max_len

    def longestIncreasingContinuousSubsequence_forward_backward(self, A):
        n = len(A)
        if n <= 2: return n
        inc_len = 1; pre = 1;
        for i in range(1, n):
            cur = 1
            if A[i] > A[i-1]:
                cur = pre + 1
            inc_len = max(inc_len, cur)
            pre = cur
        dec_len = 1; pre = 1;
        for i in range(1, n):
            cur = 1
            if A[i] < A[i-1]: cur = pre + 1
            dec_len = max(dec_len, cur)
            pre = cur
        return max(inc_len, dec_len)

    def longestIncreasingContinuousSubsequence(self, A):
        n = len(A)
        if n <= 2: return n
        res = 2; pre = 2
        for i in range(2, n):
            cur = 2
            if A[i-2] < A[i-1] < A[i] or A[i-2] > A[i-1] > A[i]:
                cur = pre + 1
            pre = cur
            res = max(res, cur)
        return res

    def findNumberOfLIS(self, nums):
        n = len(nums)
        if n == 0: return 0
        dp = [1] * n
        cnts = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        cnts[i] = cnts[j]
                        dp[i] = dp[j]+1
                    elif dp[i] == dp[j] + 1:
                        cnts[i] += cnts[j]
        res = 0; cnt = 0
        for i in range(n):
            if dp[i] > res:
                res = dp[i]
                cnt = cnts[i]
            elif dp[i] == res:
                cnt += cnts[i]
        return cnt

    def isInterleave(self, s1, s2, s3):
        n1 = len(s1)
        n2 = len(s2)
        if len(s3) != n1+n2: return False
        dp  = []
        for i in range(n1+1): dp.append([False] * (n2+1))
        dp[0][0] = True
        for i in range(1, n1+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n2+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]
        print(dp)
        return dp[n1][n2]

    def longestCommonSubsequence(self, A, B):
        n1 = len(A)
        n2 = len(B)
        dp = []
        for i in range(n1+1): dp.append([0]*(n2+1))
        res = 0
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                res = max(res, dp[i][j])
        return dp[n1][n2]



s = Solution()
A = 'ABCD'
B =  'EACB'
print(s.longestCommonSubsequence(A, B))

'''
s1="aabcc"
s2="dbbca"
s3="aadbbcbcad"
print(s.isInterleave(s1, s2, s3))


print(s.longestIncreasingContinuousSubsequence([5,4,2,1,3]))
print(s.longestIncreasingContinuousSubsequence([5,1,2,3,4]))

print(s.findNumberOfLIS([2, 2, 2, 2, 2]))
print(s.findNumberOfLIS([1, 3, 5, 4, 7]))

print(s.findNumberOfLIS([1,2,4,3,5,4,7,2]))

print(s.longestIncreasingSubsequence([5,4,1,2,3]))
print(s.longestIncreasingSubsequence([4,2,4,5,3,7]))

print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
'''
