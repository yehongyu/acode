class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.cnt_map = {}
        self.max_freq = 0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x not in self.freq:
            self.freq[x] = 0
        self.freq[x] += 1
        self.max_freq = max(self.max_freq, self.freq[x])
        if self.freq[x] not in self.cnt_map:
            self.cnt_map[self.freq[x]] = []
        self.cnt_map[self.freq[x]].append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.max_freq == 0: return None
        res = self.cnt_map[self.max_freq][-1]
        self.cnt_map[self.max_freq].pop(-1)
        if len(self.cnt_map[self.max_freq]) == 0:
            self.max_freq -= 1
        self.freq[res] -= 1
        return res

# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
