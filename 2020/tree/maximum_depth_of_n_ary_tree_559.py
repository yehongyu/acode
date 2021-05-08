"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children # list(Node)


class Solution(object):
    def maxDepthWithRecursion(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None: return 0
        max_sub_depth = 0
        for node in root.children:
            cur_depth = self.maxDepthWithRecursion(node)
            max_sub_depth = max(cur_depth, max_sub_depth)
        return max_sub_depth + 1

    def maxDepthWithQueue(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None: return 0
        max_depth = 0
        queue = []
        queue.append([root, 1])
        while len(queue) > 0:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)
            for sub_node in node.children:
                queue.append([sub_node, depth+1])
        return max_depth


