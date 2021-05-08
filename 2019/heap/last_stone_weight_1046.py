class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq
        arr = []
        for stone in stones:
            heapq.heappush(arr, -stone)
        while len(arr) >= 2:
            a = heapq.heappop(arr)
            b = heapq.heappop(arr)
            if a == b: continue
            else: heapq.heappush(arr, a-b)
        if len(arr) == 1:
            return -heapq.heappop(arr)
        return 0

s = Solution()
stones = [2,7,4,1,8,1]
print(s.lastStoneWeight(stones))

