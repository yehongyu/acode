class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n <= 1: return n
        max_idx = 0; res = 1
        for i in range(n):
            if max_idx < i: res+=1
            if arr[i] > max_idx:
                max_idx = arr[i]
        return res

s = Solution()
arr = [4,3,2,1,0]
print(s.maxChunksToSorted(
    arr
))
