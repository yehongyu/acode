class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        if n == 0: return None
        if n == 1: return arr[0]
        res1=0
        res2 = max(arr)
        acc = 0
        l = 0; h = max(arr)
        while l <= h:
            mid = l + (h-l)//2
            cur_sum = sum([min(mid, num) for num in arr])
            if cur_sum > target:
                h = mid - 1
                res2 = min(res2, mid)
            else:
                l = mid + 1
                res1 = max(res1, mid)
        cand1 = sum([min(res1, num) for num in arr])
        cand2 = sum([min(res2, num) for num in arr])
        return res1 if target - cand1 <= cand2 - target else res2


s = Solution()
#print(s.findBestValue([4,9,3], 10))
#print(s.findBestValue([2,3,5], 10))
print(s.findBestValue([60864,25176,27249,21296,20204], 56803))
