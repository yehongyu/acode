# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepthWithRecusion(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def maxDepthWithQueue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        queue = []
        queue.append([root, 1])
        max_depth = 1
        while len(queue) > 0:
            node, cur_depth = queue.pop(0)
            max_depth = max(max_depth, cur_depth)
            if node.left:
                queue.append([node.left, cur_depth+1])
            if node.right:
                queue.append([node.right, cur_depth+1])
        return max_depth


    def maxDepthWithStack(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        stack = []
        stack.append([root, 1])
        max_depth = 1
        while len(stack) > 0:
            node, cur_depth = stack.pop(-1)
            max_depth = max(max_depth, cur_depth)
            if node.right:
                stack.append([node.right, cur_depth+1])
            if node.left:
                stack.append([node.left, cur_depth+1])
        return max_depth



