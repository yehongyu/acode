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
    def connect_perfect_binary_tree(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None: return
        if root.left:
            root.left.next = root.right
        if root.right:
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
        self.connect(root.left)
        self.connect(root.right)

    def connect_tree(self, root):
        if root == None: return None

        next = None
        cur = root.next
        while cur != None:
            if cur.left:
                next = cur.left
                break
            if cur.right:
                next = cur.right
                break
            cur = cur.next
        if root.right:
            root.right.next = next
            if root.left:
                root.left.next = root.right
        elif root.left:
            root.left.next = next
        self.connect(root.left)
        self.connect(root.right)
        return root


    def connect(self, root):
        if root == None: return None
        queue = [root]
        while len(queue) > 0:
            qlen = len(queue)
            pre = None
            for i in range(qlen):
                cur = queue[0]; queue.pop(0)
                print('cur:', cur.val)
                if pre != None: pre.next = cur
                pre = cur
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return root

def show_tree(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        level_res = []
        node = queue[0]; queue.pop(0)
        while node != None:
            level_res.append(node.val)
            if len(queue) == 0:
                if node.left:
                    queue.append(node.left)
                elif node.right:
                    queue.append(node.right)
            node = node.next
        print('level:', level_res)


s = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
new_tree = s.connect(root)
show_tree(new_tree)



