# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements(object):

    def generate(self, root, data, pos):
        if root == None: return
        if len(data) <= pos:
            data.extend([False] * (pos-len(data)+1))
        data[pos] = True
        self.generate(root.left, data, pos*2 + 1)
        self.generate(root.right, data, pos*2 + 2)

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.data = []
        if root == None: return
        self.generate(root, self.data, 0)
        print(len(self.data), self.data)


    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target < 0: return False
        if len(self.data) <= target: return False
        return self.data[target]

# Your FindElements object will be instantiated and called as such:
root = TreeNode(-1)
root.left = TreeNode(-1)
root.right = TreeNode(-1)
root.left.left = TreeNode(-1)
root.left.right = TreeNode(-1)
root.right.left = TreeNode(-1)
root.right.left.right = TreeNode(-1)

obj = FindElements(root)
print(obj.find(5))
print(obj.find(6))
print(obj.find(2))
