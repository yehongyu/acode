# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def del_tree_node(self, root, to_delete, res):
        if root == None: return None
        root.left = self.del_tree_node(root.left, to_delete, res)
        root.right = self.del_tree_node(root.right, to_delete, res)
        if root.val in to_delete:
            if root.left: res.append(root.left)
            if root.right: res.append(root.right)
            return None
        else:
            return root

    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if root == None: return []
        if len(to_delete) == 0: return [root]
        res = []
        newnode = self.del_tree_node(root, set(to_delete), res)
        if newnode: res.append(newnode)
        return newnode

    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if root == None: return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None

    def longestZigZag_helper(self, root):
        if root == None: return -1, -1, -1
        if not root.left and not root.right: return 0, 0, 0
        l_l, l_r, l_max = self.removeLeafNodes(root.left)
        r_l, r_r, r_max = self.removeLeafNodes(root.right)
        l = 0; r = 0
        if root.left:
            l = l_r + 1
        if root.right:
            r = r_l + 1
        return l, r, max(l, r, l_max, r_max)

    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        return self.longestZigZag_helper(root)[2]

    def judge(self, head, root):
        if head == None: return True
        if root == None: return False
        if root.val != head.val: return False
        return self.judge(head.next, root.left) or self.judge(head.next, root.right)

    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if head == None: return True
        if root == None: return False
        if self.judge(head, root): return True
        if self.isSubPath(head, root.left): return True
        if self.isSubPath(head, root.right): return True

    def sum_helper(self, grand, father):
        if grand == None: return 0
        if father == None: return 0
        res = 0
        if father.left:
            res += self.sum_helper(father, father.left)
            if grand.val % 2 == 0:
                res += father.left
        if father.right:
            res += self.sum_helper(father, father.right)
            if grand.val % 2 == 0:
                res += father.right
        return res

    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        res = 0
        res += self.sum_helper(root, root.left)
        res += self.sum_helper(root, root.right)
        return res



