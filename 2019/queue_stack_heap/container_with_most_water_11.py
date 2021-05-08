class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 1: return 0
        res = 0
        l = 0; r = n - 1
        while l < r:
            cur_h = min(height[l], height[r])
            cur_area = cur_h * (r - l)
            res = max(res, cur_area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(height))
