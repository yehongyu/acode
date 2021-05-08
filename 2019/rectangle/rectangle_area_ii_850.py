#coding=utf-8

class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        all = []
        for cur in rectangles:
            self.helper(all, cur, 0)
        sum = 0
        print(all)
        for rect in all:
            sum = (sum + (rect[3] - rect[1]) * (rect[2] - rect[0])) % 1000000007
        return sum

    def helper(self, all, cur, index):
        if index >= len(all):
            all.append(cur[0:])
            return
        rect = all[index]
        if rect[2] <= cur[0] or rect[0] >= cur[2] or \
                rect[3] <= cur[1] or rect[1] >= cur[3]:
            self.helper(all, cur, index+1)
            return
        if rect[0] > cur[0]:
            self.helper(all, [cur[0], cur[1], rect[0], cur[3]], index+1)
        if rect[2] < cur[2]:
            self.helper(all, [rect[2], cur[1], cur[2], cur[3]], index+1)
        if rect[1] > cur[1]:
            self.helper(all, [max(rect[0], cur[0]), cur[1], min(rect[2], cur[2]), rect[1]], index+1)
        if rect[3] < cur[3]:
            self.helper(all, [max(rect[0], cur[0]), rect[3], min(rect[2], cur[2]), cur[3]], index+1)




s = Solution()
'''
rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
print(s.rectangleArea(rectangles))
rectangles = [[0,0,1000000000,1000000000]]
print(s.rectangleArea(rectangles))
'''
rectangles = [[49,40,62,100],[11,83,31,99],[19,39,30,99]]
print(s.rectangleArea(rectangles))
