class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0 or n2 == 0: return []
        res = []
        i = 0; j = 0
        for t in range(k):
            if i < n1 or j < n2:
                res.append([nums1[i], nums2[j]])
                if i + 1 < n1 and j + 1 < n2:
                    if nums1[i+1] <= nums2[j+1]:
                        i += 1
                    else:
                        j += 1
                elif i + 1 < n1:
                    i += 1
                elif j + 1 < n2:
                    j += 1
                else: break
            else: break
        return res


s = Solution()
nums1 = [1,7,11]; nums2 = [2,4,6]; k = 3
nums1 = [1,1,2]; nums2 = [1,2,3]; k = 10
print(s.kSmallestPairs(nums1, nums2, k))

