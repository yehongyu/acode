# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def convert(self, root, arr):
        if root == None: return
        if root.left:
            self.convert(root.left, arr)
        arr.append(root.val)
        if root.right:
            self.convert(root.right, arr)

    def merge(self, arr1, arr2, arr3):
        m = len(arr1)
        n = len(arr2)
        i  =0; j = 0
        while i < m or j < n:
            if i< m and j < n:
                if arr1[i] < arr2[j]:
                    arr3.append(arr1[i]); i+=1
                else:
                    arr3.append(arr2[j]); j+=1
            elif i < m:
                arr3.append(arr1[i]); i+=1
            elif j < n:
                arr3.append(arr2[j]); j+=1

    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        arr1 = []
        self.convert(root1, arr1)
        arr2 = []
        self.convert(root2, arr2)
        arr3 = []
        self.merge(arr1, arr2, arr3)
        return arr3

s = Solution()
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)
print(s.getAllElements(root1, root2))
