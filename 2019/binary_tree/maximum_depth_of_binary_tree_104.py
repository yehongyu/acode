#coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth_recursion(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def maxDepth_preorder_stack(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        stack = []
        stack.append([root, 1])
        res = 1
        while len(stack) > 0:
            node, depth = stack[-1]
            res = max(res, depth)
            stack.pop(-1)
            if node.left != None:
                stack.append([node.left, depth+1])
            if node.right != None:
                stack.append([node.right, depth+1])
        return res

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        queue = []
        queue.append([root, 1])
        res = 1
        while len(queue) > 0:
            node, depth = queue[0]
            res = max(res, depth)
            queue.pop(0)
            if node.left != None:
                queue.append([node.left, depth+1])
            if node.right != None:
                queue.append([node.right, depth+1])
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)

s = Solution()
print(s.maxDepth(root))
print(s.maxDepth(root.left))

