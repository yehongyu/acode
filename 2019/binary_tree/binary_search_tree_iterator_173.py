# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        cur = root
        while cur != None:
            self.stack.append(cur)
            cur = cur.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        res = None
        if not self.hasNext(): return res
        cur = self.stack[-1]; self.stack.pop(-1)
        res = cur.val
        cur = cur.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()