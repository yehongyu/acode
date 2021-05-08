class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        n = len(houses)
        m = len(heaters)
        if n <= 0 or m <= 0: return -1
        houses = sorted(houses)
        heaters = sorted(heaters)
        j = 0
        res = 0
        for i in range(n):
            while j < m-1 and abs(heaters[j]-houses[i]) >= abs(heaters[j+1]-houses[i]):
                j += 1
            res = max(res, abs(heaters[j]-houses[i]))
        return res

s = Solution()
houses = [1,2,3]
heaters = [2]
houses = [1,2,3,4]
heaters = [1,4]
print(s.findRadius(houses, heaters))
