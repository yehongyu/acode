#coding=utf-8

class Node(object):
    def __init__(self, val, smaller=0):
        self.val = val
        self.smaller = smaller
        self.left = None
        self.right = None

class Solution(object):
    # n * n
    def countSmaller_brute_force(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0] * len(nums)
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    count[i] += 1
        return count

    # n * log(n)
    def countSmaller_insert_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = []
        count = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            low = 0; high = len(tmp)
            key = nums[i]
            while low < high:
                mid = low + (high-low)/2
                if key > tmp[mid]:
                    low = mid + 1
                else:
                    high = mid

            count[i] = high
            tmp.insert(high, key)
        return count

    def insert_tree_node(self, root, val):
        if root is None:
            return 0
        if root.val >= val:
            cur_samller = root.smaller
            root.smaller += 1
            if root.left is None:
                root.left = Node(val)
                return cur_samller
            else:
                return self.insert_tree_node(root.left, val)
        else:
            if root.right is None:
                root.right = Node(val)
                return root.smaller + 1
            else:
                return self.insert_tree_node(root.right, val) + 1


    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 0:
            return []
        count = [0] * len(nums)
        root = Node(nums[len(nums)-1])
        for i in range(len(nums) - 2, -1, -1):
            count[i] = self.insert_tree_node(root, nums[i])
            print(i, count[i])
        return count



s = Solution()
nums = [2, 0, 1]
nums = [5, 2, 6, 1]
nums = [0, 1, 2]
print(s.countSmaller(nums))

