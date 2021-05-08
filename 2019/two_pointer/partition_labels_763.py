class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        n = len(S)
        if n == 1: return [0]
        ch_map = {}
        for i in range(n):
            ch_map[S[i]] =i
        end = 0
        start = 0
        for i in range(n):
            ch = S[i]
            end = max(end, ch_map[ch])
            if end == i:
                res.append(end - start + 1)
                start = end + 1
        return res

s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))

