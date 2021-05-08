# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def judge(self, r1, r2):
        if not r1 and not r2: return True
        if not r1 or not r2: return False
        if r1.val != r2.val: return False
        return self.judge(r1.left, r2.left) and self.judge(r1.right, r2.right)

    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if not cloned: return None
        if not target: return None
        if self.judge(cloned, target): return cloned
        res = self.getTargetCopy(original, cloned.left, target)
        if res: return res
        res = self.getTargetCopy(original, cloned.right, target)
        if res: return res
