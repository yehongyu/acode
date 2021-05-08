class Solution():
    def largestRectangleInHistogram(self, heights):
        size = len(heights)
        if size <= 0: return 0
        if size == 1: return heights[0]
        stack = []
        max_area = 0
        heights.append(-1)
        for i in range(size+1):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                start = stack.pop(-1)
                end = i-1
                area = (end-start+1) * heights[start]
                print(start, end, heights[start], heights[end])
                max_area = max(max_area, area)
            if i < size:
                stack.append(i)
                print("stack", stack)
        return max_area

if __name__ == "__main__":
    s = Solution()
    heights = [2,1,5,6,2,3, 7,8]
    res = s.largestRectangleInHistogram(heights)
    print(res)
