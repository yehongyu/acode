class Solution(object):
    def get_root(self, finder, key):
        if key not in finder:
            finder[key] = key
            return key
        while finder[key] != key:
            key = finder[key]
        return key
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        finder = {}
        n = len(equations)
        for i in range(n):
            equ = equations[i]
            if equ[1:3] == '==':
                a = self.get_root(finder,equ[0])
                b = self.get_root(finder,equ[3])
                if a!= b:
                    finder[a] = b
                    print(finder)
        for i in range(n):
            equ = equations[i]
            if equ[1:3] == '!=':
                a = self.get_root(finder,equ[0])
                b = self.get_root(finder,equ[3])
                print(equ, a, b)
                if a == b:
                    return False
        return True

s = Solution()
equas = ["a==b","b!=a"]
print(s.equationsPossible(equas))