class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n <= 0: return 0
        if n == 1: return heights[0]
        stack = []
        res = heights[0]
        for i in range(n+1):
            while len(stack)>0 and (i>=n or heights[stack[-1]] >= heights[i]):
                top = stack[-1]; stack.pop(-1)
                area = (i-1-(stack[-1] if len(stack)>0 else -1)) * heights[top]
                res = max(res, area)
            stack.append(i)
        return res

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m <= 0: return 0
        n = len(matrix[0])
        heights = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            cur = self.largestRectangleArea(heights)
            res = max(res, cur)
        return res



s = Solution()
heights = [2,1,5,6,2,3]
#print(s.largestRectangleArea(heights))

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
matrix = [["0","1"],["1","0"]]
print(s.maximalRectangle(matrix))


