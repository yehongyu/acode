"""
Definition of Doubly-ListNode
"""
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = None
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def helper(self, root):
        if root == None: return None
        cur_node = DoublyListNode(root.val)
        if root.left == None and root.right == None:
            return cur_node, cur_node
        if root.right:
            r_s, r_e = self.helper(root.right)
            cur_node.next = r_s
            r_s.prev = cur_node
        if root.left:
            l_s, l_e = self.helper(root.left)
            cur_node.prev = l_e
            l_e.next = cur_node
        if root.left and root.right:
            return l_s, r_e
        if root.left:
            return l_s, cur_node
        if root.right:
            return cur_node, r_e

    def bstToDoublyList(self, root):
        # write your code here
        if root == None: return None
        start, end = self.helper(root)
        return start

def show_tree(root):
    if root == None:
        return
    queue = [root]
    i = 0
    while len(queue) > 0:
        i += 1
        qlen = len(queue)
        for i in range(qlen):
            node = queue[0]; queue.pop(0)
            print(node.val, end=' ')
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        print('endl')

def show_double_list(head):
    cur = head
    while cur != None:
        print(cur.val, end=' ')
        cur = cur.next
    print('endl')

s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
show_tree(root)
d_l = s.bstToDoublyList(root)
show_double_list(d_l)

