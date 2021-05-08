class Solution(object):

    def dfs(self, price, special, needs, mem):
        if str(needs) in mem:
            return mem[str(needs)]
        res = 0
        for i in range(len(needs)):
            res += needs[i] * price[i]
        for sp in special:
            nn = needs[0:]
            flag = True
            for i in range(len(nn)):
                nn[i] -= sp[i]
                if nn[i] < 0:
                    flag = False
                    break
            if flag:
                res = min(res, sp[-1] + self.dfs(price, special, nn, mem))
        mem[str(needs)] = res
        return res

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        mem = {}
        res = self.dfs(price, special, needs, mem)
        return res

s = Solution()
price =[2,5]; special = [[3,0,5], [1,2,10]]; needs = [3,2]
price = [2,3,4]; special = [[1,1,0,4],[2,2,1,9]]; needs = [1,2,1]
print(s.shoppingOffers(price, special, needs))

