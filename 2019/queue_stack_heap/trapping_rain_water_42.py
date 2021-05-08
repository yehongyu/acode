class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2: return 0
        stack = [0]
        res = 0
        for i in range(1, n):
            while len(stack) > 0 and height[stack[-1]] <= height[i]:
                low_i = stack[-1]; stack.pop(-1)
                if len(stack) > 0:
                    delta_h = (min(height[stack[-1]], height[i]) - height[low_i])
                    delta_w = i - stack[-1] - 1
                    res += delta_h * delta_w
            stack.append(i)
        return res

s = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(height))
