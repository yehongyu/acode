class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0 or n2 == 0: return []
        heap = []
        for i in range(n1):
            heapq.heappush(heap, [nums1[i]+nums2[0], i, 0])
        res = []
        for t in range(k):
            if len(heap) == 0: break
            cur_sum, idx1, idx2 = heapq.heappop(heap)
            res.append([nums1[idx1], nums2[idx2]])
            if idx2+1 < n2:
                heapq.heappush(heap, [nums1[idx1]+nums2[idx2+1], idx1, idx2+1])
        return res

s = Solution()
nums1 = [1,7,11]; nums2 = [2,4,6]; k = 3
print(s.kSmallestPairs(nums1, nums2, k))