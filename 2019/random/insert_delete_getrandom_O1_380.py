class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map: return False
        idx = len(self.arr)
        self.arr.append(val)
        self.map[val] = idx
        print('insert', self.map, self.arr)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map: return False
        idx = self.map[val]
        self.map.pop(val)
        if len(self.arr) > 1:
            self.map[self.arr[-1]] = idx
            self.arr[idx] = self.arr[-1]
        self.arr.pop(-1)
        print('remove', self.map, self.arr)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        rdx = random.randint(0, len(self.arr)-1)
        print('get random', self.arr, rdx)
        return self.arr[rdx]

s = RandomizedSet()
print('rm', s.remove(0))
print('rm', s.remove(0))
print('in', s.insert(0))
print('rdn', s.getRandom())
print('rm', s.remove(0))
print('in', s.insert(0))
print('rn', s.getRandom())
