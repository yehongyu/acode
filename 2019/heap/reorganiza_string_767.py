class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        import heapq
        map = {}
        n = len(S)
        for ch in S:
            if ch not in map: map[ch] = 0
            map[ch] += 1
        heap = []
        for ch in map.keys():
            if map[ch] > (n+1) // 2: return ''
            heapq.heappush(heap, [-map[ch], ch])
        res = ''
        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)
            if -cnt1-1 > 0:
                heapq.heappush(heap, [cnt1+1, ch1])
            if -cnt2-1 > 0:
                heapq.heappush(heap, [cnt2+1, ch2])
            res += ch1 + ch2
            print(res, heap, map)
        if len(heap) > 0:
            res += heapq.heappop(heap)[1]
        return res

s = Solution()
#print(s.reorganizeString('aab'))
#print(s.reorganizeString('aaab'))
print(s.reorganizeString('baaba'))
