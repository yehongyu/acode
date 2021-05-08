"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        if root == None:
            return
        cur = root
        while cur != None:
            self.stack.append(cur)
            cur = cur.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        if len(self.stack) == 0:
            return None
        node = self.stack[-1]
        self.stack.pop(-1)
        cur = node.right
        while cur != None:
            self.stack.append(cur)
            cur = cur.left
        return node


"""
Example of iterate a tree:
"""

root = TreeNode(1)
root.left = TreeNode(-3)
root.right = TreeNode(8)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)


iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    print(node.val)
