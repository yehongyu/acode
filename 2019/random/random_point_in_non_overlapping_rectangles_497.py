class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.w = [0]
        for rect in rects:
            cur = (rect[2]-rect[0]+1) * (rect[3]-rect[1]+1)
            self.w.append(self.w[-1]+cur)

    def pick(self):
        import random
        rdx = random.randint(0, self.w[-1]-1)
        l = 0; h=len(self.w)-1
        pos = None
        while l < h:
            mid = l + (h-l)//2
            if self.w[mid] == rdx:
                pos = mid; break
            elif self.w[mid] < rdx:
                l = mid + 1
            else: h = mid
        if pos == None: pos = h-1
        row = random.randint(self.rects[pos][0], self.rects[pos][2])
        col = random.randint(self.rects[pos][1], self.rects[pos][3])
        return [row, col]

s = Solution([[1,1,5,5]])
print(s.pick())
print(s.pick())
print(s.pick())
