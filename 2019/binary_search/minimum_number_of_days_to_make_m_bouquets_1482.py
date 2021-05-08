'''
Logic:
We can use binary search, but how can we get the idea to use binary search?
Actually, I use the idea from this Discusses.
If there is minimum days, the minimum days must be between
 the minimum bloom day and the maximum bloom day,
 So we can use binary search to traverse the range.
 We will check each mid days, if bloom day is less than or equal to the mid day,
 then we can use this flower to consist the bouquet.
 When the number of flowers in current bouquet is equal to k,
 we reset the flower_cnt to construct a new bouquet.
 If current bloom day is greater than mid day, then we canot use this flower,
 as it hasn't bloomed. So we need to reset the flower_cnt, and to construct a new bouquet.
 If the number of bouquets is greater than m, it means in mid days we can have m bouquet.


'''


class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m <= 0 or k <= 0 or len(bloomDay) < m * k: return -1
        l = min(bloomDay); r = max(bloomDay)
        while l < r:
            mid = l + int((r-l)/2)
            if self.check(bloomDay, m, k, mid):
                r = mid
            else:
                l = mid + 1
        return r

    def check(self, bloomDay, m, k, mid):
        flower_cnt = 0; bouquet_cnt = 0
        for val in bloomDay:
            if val <= mid:
                flower_cnt += 1
                if flower_cnt >= k:
                    bouquet_cnt += 1
                    flower_cnt = 0
            else:
                flower_cnt = 0
        if bouquet_cnt >= m: return True
        return False

s = Solution()
bloomDay = [1,10,3,10,2]; m = 3; k = 1 # 3
bloomDay = [1,10,3,10,2]; m = 3; k = 2 # -1
bloomDay = [7,7,7,7,12,7,7]; m = 2; k = 3 # 12
bloomDay = [1000000000,1000000000]; m = 1; k = 1 # 100000000
bloomDay = [1,10,2,9,3,8,4,7,5,6]; m = 4; k = 2 # 9
res = s.minDays(bloomDay, m, k)
print(res)