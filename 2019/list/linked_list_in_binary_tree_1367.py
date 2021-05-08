#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def judge(self, head, root):
        if head == None: return True
        if root == None: return False
        if head.val != root.val: return False
        return self.judge(head.next, root.left) or self.judge(head.next, root.right)

    def isSubPath(self, head, root):
        if head == None: return True
        if root == None: return False
        if self.judge(head, root):
            return True
        if root.left:
            if self.isSubPath(head, root.left): return True
        if root.right:
            return self.isSubPath(head, root.right)



