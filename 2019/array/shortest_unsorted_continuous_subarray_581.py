class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1: return 0
        if n == 2: return 0 if nums[1] >= nums[0] else 2
        l = 1
        while l < n and nums[l] >= nums[l-1]:
            l+=1
        if l==n: return 0
        r = n-2
        while r>=0 and nums[r] <= nums[r+1]:
            r-=1
        if r<0: return 0
        print('ee', l, r)
        tl = min(l, r)
        tr = max(l, r)
        m_min = nums[tl]
        m_max = nums[tl]
        for i in range(tl, tr+1):
            m_min = min(m_min, nums[i])
            m_max = max(m_max, nums[i])
        print('mid', m_min, m_max)
        tl -= 1; tr += 1
        while tl >=0 and nums[tl] > m_min:
            tl-=1
        while tr < n and nums[tr] < m_max: tr+=1
        print('end', tl, tr)
        return tr - tl -1

s = Solution()
nums = [2, 6, 4, 8, 10, 9, 15]
nums = [2,1]
nums = [1,3,2,4,5]
nums = [2,3,3,2,4]
nums = [1,2,3,3,3]
nums = [1,3,2,3,3]
print(s.findUnsortedSubarray(nums))
