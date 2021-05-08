class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = len(dominoes)
        dist = [0] * n
        i = 0; start = None
        res = list(dominoes[0:])
        for i in range(1, n):
            if dominoes[i] == '.' and res[i-1] == 'R':
                dist[i] = dist[i-1] + 1
                res[i] = 'R'
                print(i, res)
        pre = 0
        for i in range(n-2, -1, -1):
            if dominoes[i] == '.' and res[i+1] == 'L':
                pre = pre + 1
                if dist[i] == 0:
                    res[i] = 'L'
                elif dist[i]>0:
                    print(i, dist[i], pre)
                    if dist[i]>pre: res[i] = 'L'
                    elif dist[i]==pre: res[i] = '.'
            else: pre = 0
            print(i, res)
        print(res)
        return res

s = Solution()
dominoes = ".L.R...LR..L.."
print(s.pushDominoes(dominoes))



