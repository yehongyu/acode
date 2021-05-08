#coding=utf-8

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (D-B) * (C-A)
        area2 = (H-F) * (G-E)
        if E >= C or F >= D or B >= H or A >= G:
            return area1 + area2
        inter = (min(H, D) - max(B, F)) * (min(C, G) - max(A, E))
        return (area1 - inter + area2)

s = Solution()
A = -3; B = 0; C = 3; D = 4; E = 0; F = -1; G = 9; H = 2

print(s.computeArea(A, B, C, D, E, F, G, H))
A=-2
B=-2
C=2
D=2
E=3
F=3
G=4
H=4
print(s.computeArea(A, B, C, D, E, F, G, H))
