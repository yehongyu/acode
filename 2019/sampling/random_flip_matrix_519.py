#coding=utf-8


class Solution1(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.num = []
        for i in range(n_rows):
            self.num.append([0] * n_cols)

    def flip(self):
        """
        :rtype: List[int]
        """
        sum_num = sum(sum(i) for i in self.num)
        if sum_num == self.n_rows * self.n_cols:
            return
        import random
        while True:
            x = random.randint(0, self.n_rows-1)
            y = random.randint(0, self.n_cols-1)
            if self.num[x][y] == 0:
                self.num[x][y] = 1
                return [x, y]


    def reset(self):
        """
        :rtype: None
        """
        for i in range(len(self.num)):
            for j in range(len(self.num[0])):
                self.num[i][j] = 0

class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.size = n_rows * n_cols
        self.fliped = set()

    def flip(self):
        """
        :rtype: List[int]
        """
        import random
        rnd = random.randint(0, self.size-1)
        while rnd in self.fliped:
            rnd = random.randint(0, self.size-1)
        self.fliped.add(rnd)
        return [rnd / self.n_cols, rnd % self.n_cols]


    def reset(self):
        """
        :rtype: None
        """
        self.fliped.clear()



# Your Solution object will be instantiated and called as such:
n_rows = 2
n_cols = 3
obj = Solution(n_rows, n_cols)
print(obj.flip())
print(obj.flip())
print(obj.flip())
obj.reset()