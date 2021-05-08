class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea_old(self, height):
        # write your code here
        n = len(height)
        if n <= 0:
            return 0
        if n == 1:
            return height[0]
        stack = []
        res = 0
        for i in range(n+1):
            if i == n:
                while len(stack) > 0:
                    idx = stack[-1]
                    stack.pop(-1)
                    start = -1 if len(stack) == 0 else stack[-1]
                    res = max(res, height[idx] * (i-start-1))
                    print('pop, last', idx, res, stack)
                break
            if len(stack) == 0:
                stack.append(i)
                print('push, empyt', i, height[i], stack)
            elif height[i] > height[stack[-1]]:
                stack.append(i)
                print('push, >', i, height[i], stack)
            else:
                while len(stack) > 0 and height[i] <= height[stack[-1]]:
                    idx = stack[-1]
                    stack.pop(-1)
                    start = -1 if len(stack) == 0 else stack[-1]
                    res = max(res, height[idx] * (i-start-1))
                    print('pop', i, idx, res, stack)
                stack.append(i)
                print('push', i, res, stack)
        return res


    def largestRectangleArea(self, height):
        # write your code here
        n = len(height)
        if n <= 0: return 0
        if n == 1: return height[0]
        stack = [0]
        res = height[0]
        for i in range(1, n+1):
            while len(stack) > 0 and (i >= n or height[i] <= height[stack[-1]]):
                cur_idx = stack[-1]; stack.pop(-1)
                if len(stack) == 0:
                    start_idx = 0
                else:
                    start_idx = stack[-1] + 1
                cur_h = height[cur_idx]
                w = i - start_idx
                res = max(res, w*cur_h)
            if i < n:
                stack.append(i)
        return res





s = Solution()
#print(s.largestRectangleArea([1, 1]))
#print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(s.largestRectangleArea([5, 4, 1, 2]))
