class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        if n <= 1: return []
        l = 0; r = n-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target: return [l, r]
            elif sum > target: r -= 1
            else: l += 1
        return []

    def minSubArrayLen(self, s, nums):
        n = len(nums)
        if n <= 0: return 0
        res = n+1
        l = 0; r = 0
        sum = 0
        while l <= r and l < n and r <= n:
            print(l, r, res, sum)
            if sum < s and r < n:
                sum += nums[r]
                r += 1
            elif sum >= s:
                res = min(res, r-l)
                sum -= nums[l]
                l += 1
            else:
                l += 1
        return res if res < n+1 else 0

    def findLength(self, A, B):
        m = len(A)
        n = len(B)
        dp = []
        for i in range(m): dp.append([0] * n)
        res = 0
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    if i-1>=0 and j-1>=0: dp[i][j] = dp[i-1][j-1] + 1
                    else: dp[i][j] = 1
                res = max(res, dp[i][j])
        return res

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def findDuplicate_mutable(self, nums):
        n = len(nums) - 1
        if n == 0: return nums[0]
        i = 0
        while i < n:
            if nums[i] != i+1:
                if nums[nums[i]-1] == nums[i]:
                    return nums[i]
                self.swap(nums, i, nums[i]-1)
            else:
                i += 1
        return nums[n]

    def findDuplicate(self, nums):
        n = len(nums) - 1
        if n == 0: return nums[0]
        l = 1; r = n
        while l < r:
            mid = l + (r-l)//2
            cnt = 0;
            for num in nums:
                if num <= mid: cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid
        return r

    def characterReplacement(self, s, k):
        n = len(s)
        if n <= k: return n
        ch_map = {}
        start = 0; maxch = 0
        for i in range(n):
            ch  = s[i]
            if ch not in ch_map:ch_map[ch] = 0
            ch_map[ch] += 1
            maxch = max(maxch, ch_map[ch])
            while i - start + 1 - maxch > k:
                ch_map[s[start]] -= 1
                start += 1
            res = max(res, i-start+1)
        return res

    def longestOnes(self, A, K):
        n = len(A)
        ch_map = {0:0,1:0}
        res=0; start=0
        for i in range(n):
            ch_map[A[i]] += 1
            max_cnt = ch_map[1]
            while i - start + 1 - max_cnt > K:
                ch_map[A[start]] -= 1
                start += 1
            res = max(res, i - start + 1)
        return res

    def circularArrayLoop(self, nums):
        n = len(nums)
        visited = [False] * n
        if n<= 1: return False
        for i in range(n):
            cur = i
            visited[i] = True
            mapping = {}
            while True:
                next = (cur + nums[cur]) % n
                if next == cur: break
                if nums[next] * nums[cur]<=0: break
                if next in mapping: return True
                mapping[cur] = next
                cur = next
                visited[cur] = True
            print(i, visited)
        return False

    def canMatch(self, s, target):
        m = len(s)
        n = len(target)
        if m < n: return False
        i = 0; j=0
        while i < m and j < n:
            if s[i] == target[j]:
                i += 1; j += 1
            else:
                i += 1
        return j == n

    def findLongestWord(self, s, d):
        result = ''
        n = len(d)
        for target in d:
            if len(target) < len(result): continue
            if len(target) == len(result) and result <= target: continue
            if self.canMatch(s, target):
                result = target
        return result

    def checkInclusion(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2: return False
        ch_map = {}
        for ch in s2:
            ch_map[ch] = 0
        for ch in s1:
            if ch not in ch_map:
                ch_map[ch] = 0
            ch_map[ch] += 1
        start = 0
        for i in range(n2):
            ch = s2[i]
            ch_map[ch] -= 1
            if ch_map[ch] < 0:
                while True:
                    ch_map[s2[start]] += 1
                    start += 1
                    if ch_map[s2[start-1]] == 0:
                        break
            else:
                if i-start+1 == n1: return True
        return False

    def findAnagrams(self, s, p):
        n1 = len(s)
        n2 = len(p)
        if n1 < n2: return []
        res = []
        map = {}
        for ch in s: map[ch] = 0
        for ch in p:
            if ch not in map: map[ch] = 0
            map[ch] += 1
        start = 0
        for i in range(n1):
            ch = s[i]
            map[ch] -= 1
            print(i, ch, start, map)
            if map[ch] < 0:
                while start <= i and map[s[start]] != 0:
                    map[s[start]] += 1
                    start += 1
                    if n2 == i - start + 1: res.append(i-n2+1)
            else:
                if n2 == i - start + 1: res.append(i-n2+1)
        return res

    def numSubarrayProductLessThanK(self, nums, k):
        if k <=0: return 0
        n = len(nums)
        l = 0; r=0; product = 1
        res = 0
        while l <= r and l < n and r <= n:
            print(l, r, product)
            if product < k and r < n:
                product *= nums[r]
                r += 1
            else:
                if product >= k:
                    res += r-l-1
                else:
                    res += r -l
                product /= nums[l]
                l += 1
        return res





so = Solution()
nums = [10, 5, 2, 6]
k = 100
nums = [1,2,3]
nums = [1,1,1]
k=1
print(so.numSubarrayProductLessThanK(nums, k))
'''
print(so.findAnagrams("baa", "aa"))
#print(so.findAnagrams("aa", "bb"))
#print(so.findAnagrams("abab", "ab"))
#print(so.findAnagrams("cbaebabacd", "abc"))
print(so.checkInclusion('ab', "eidboaooo"))
s = "abpcplea"
d = ["ale","apple","monkey","plea"]
print(so.findLongestWord(s, d))
nums = [2,-1,1,2,2]
nums = [-1, 2]
nums = [-2,1,-1,-2, -2]
print(so.circularArrayLoop(nums))
nums = [1,3,4,2,2]
print(so.findDuplicate(nums))
s = 7
nums = [2,3,1,2,4,3]
print(so.minSubArrayLen(s, nums))
'''
