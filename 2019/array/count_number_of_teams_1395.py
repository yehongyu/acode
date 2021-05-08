class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        if n < 3: return 0
        res = 0
        for i in range(1, n-1):
            l_small = 0
            l_great = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    l_small += 1
                elif rating[j] > rating[i]:
                    l_great += 1
            r_small = 0
            r_great = 0
            for j in range(i+1, n):
                if rating[j] < rating[i]:
                    r_small += 1
                elif rating[j] > rating[i]:
                    r_great += 1
            res += l_small * r_great
            res += l_great * r_small
        return  res

s = Solution()
rating = [2,1,3]
rating = [1,2,3,4]
rating = [2,5,3,4,1]
print(s.numTeams(rating))

