#coding=utf-8

class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.nums = arr[0:]

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        map = {}
        for i in range(left, right+1):
            key = self.nums[i]
            if key not in map:
                map[key] = 0
            map[key] += 1
        res = -1
        for val in map.keys():
            if map[val] >= threshold:
                return val
        return res


# Your MajorityChecker object will be instantiated and called as such:
'''
arr = [1, 1, 2, 2, 1, 1]
obj = MajorityChecker(arr)
print(obj.query(0, 5, 4))
print(obj.query(0, 3, 3))
print(obj.query(2, 3, 2))
'''
arr = [2, 2, 1, 2, 1, 2, 2, 1, 1, 2]
obj = MajorityChecker(arr)
print(obj.query(0, 1, 2))


