class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sw = [0]
        for i in range(len(w)):
            self.sw.append(self.sw[-1] + w[i])
        print(self.sw)

    def pickIndex(self):
        import random
        key = random.randint(0, self.sw[-1]-1)
        l = 0; h = len(self.sw)-1
        while l < h:
            mid = l + (h-l)//2
            #print(key, l, h, mid)
            if self.sw[mid] == key: return mid
            elif self.sw[mid] < key:
                l = mid + 1
            else: h = mid
        return h-1

s = Solution([1,5,3])
map = {}
for i in range(90000):
    idx = s.pickIndex()
    if idx not in map: map[idx] = 0
    map[idx] += 1
print(map)
