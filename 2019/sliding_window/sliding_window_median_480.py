#coding=utf-8

class Solution(object):
    def medianSlidingWindow_fore_brute(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if len(nums) <= 0:
            return nums
        res = []
        for i in range(len(nums)-k+1):
            window = nums[i:i+k]
            window = sorted(window)
            if k % 2 == 1:
                res.append(window[k/2])
            else:
                res.append((window[(k-1)/2] + window[k/2])/2)
        return res

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        res = []
        import bisect
        if len(nums) <= 0:
            return nums
        res = []
        window = nums[0:k]
        window.sort()
        print(window)
        mid = window[k/2] if k%2==1 else (window[k/2-1]+window[k/2])/2.0
        res.append(mid)
        for i in range(k, len(nums)):
            window.remove(nums[i-k])
            bisect.insort(window, nums[i])
            mid = window[k/2] if k%2==1 else (window[k/2-1]+window[k/2])/2.0
            res.append(mid)
        return res






s = Solution()
print(s.medianSlidingWindow([1,4,2,3], 4))
#print(s.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
