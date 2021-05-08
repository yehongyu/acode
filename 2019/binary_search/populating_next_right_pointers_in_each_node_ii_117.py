"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        if root == None: return None
        queue = [root]
        while len(queue) > 0:
            qlen = len(queue)
            pre = None
            for i in range(qlen):
                cur = queue[0]; queue.pop(0)
                if pre:
                    pre.next = cur
                pre = cur
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return root


