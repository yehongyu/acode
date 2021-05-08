"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
Definition for singly-linked list.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if root == None: return []
        queue = [root]
        res = []
        while len(queue) > 0:
            qlen = len(queue)
            node = queue[0]; queue.pop(0)
            head = ListNode(node.val)
            cur = head
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            for i in range(1, qlen):
                node = queue[0]; queue.pop(0)
                listNode = ListNode(node.val)
                cur.next = listNode
                cur = cur.next
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(head)
        return res

def show_list(head):
    cur = head
    while cur != None:
        print(cur.val, end=' ')
        cur = cur.next
    print('endl')


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
res = s.binaryTreeToLists(root)
for l in res:
    show_list(l)

