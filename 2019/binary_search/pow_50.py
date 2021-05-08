class Solution(object):
    def myPow_other(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if n == 1: return x
        if n == -1: return 1/x
        m = int(n / 2)
        cur = self.myPow(x, m)
        cur = cur * cur
        if n % 2 == 0:
            return cur
        else:
            if n < 0:
                return cur * 1/x
            else:
                return cur * x

    def myPow(self, x, n):
        if n == 0: return 1
        if n == 1: return x
        if n < 0:
            return self.myPow(1/x, -n)
        m = n // 2
        cur = self.myPow(x, m)
        if n % 2 == 1:
            return cur * cur * x
        else:
            return cur * cur

    def mySqrt(self, x):
        if x < 0: return None
        if x <= 1: return x
        l = 1; h = x
        res = 1
        while l <= h:
            mid = l + (h - l) // 2
            cur = mid * mid
            print(l, h, mid, cur)
            if cur > x:
                h = mid - 1
            elif cur < x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res

    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0: return 0
        dp = []
        for i in range(n):
            dp.append([1]*n)
        res = 0
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                res = max(dp[i], res)
        return res

    def search_pos(self, nums, val):
        n = len(nums)
        l = 0; r = n-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > val:
                r = mid
            else:
                l = mid + 1
        if nums[r] > val: return r
        else:
            return r + 1

    def kthSmallest(self, matrix, k):
        n = len(matrix)
        if n * n < k: return -1
        l = matrix[0][0]; r = matrix[n-1][n-1]
        while l < r:
            mid = l + (r-l)//2
            cnt = 0
            for i in range(n):
                pos = self.search_pos(matrix[i], mid)
                print(mid, i, pos)
                cnt += pos
            print(l, r, mid, cnt)
            if cnt < k: l = mid + 1
            else: r = mid
        return l

    def isSubsequence(self, s, t):
        m = len(s)
        n = len(t)
        if m > t: return False
        i=0; j =0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1; j += 1
            else:
                j += 1
        if i == m and j <= n: return True
        else: return False

    def findClosestElements(self, arr, k, x):
        n = len(arr)
        if n < k or k <= 0: return []
        l = 0; r = n-1
        while r - l + 1 > k:
            diff1 = abs(arr[l] - x)
            diff2 = abs(arr[r] - x)
            if diff1 <= diff2:
                r -= 1
            else:
                l += 1
        return arr[l:r+1]

    def minEatingSpeed(self, piles, H):
        n = len(piles)
        if n > H: return -1
        piles = sorted(piles)
        l = 1; h = piles[-1]
        while l < h:
            mid = l + (h-l)//2
            cur_h = 0
            for pile in piles: cur_h += (pile + mid - 1) // mid
            print(l, h, mid, cur_h)
            if cur_h > H: l = mid + 1
            else: h = mid
        return h

    def shipWithinDays(self, weights, D):
        n = len(weights)
        if n <= 0 or D <= 0: return 0
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = l + (r-l) // 2
            days = 1; cur = mid
            for w in weights:
                if cur - w < 0:
                    days += 1
                    cur = mid
                cur -= w
            if days > D: l = mid + 1
            else: r = mid
        return r



s = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]; D = 5
print(s.shipWithinDays(weights, D))
'''
piles = [30,11,23,4,20]; H = 5
print(s.minEatingSpeed(piles, H))

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(s.kthSmallest(matrix, k))

#print(s.mySqrt(5))
#print(s.myPow(34.00515, -3))

'''

