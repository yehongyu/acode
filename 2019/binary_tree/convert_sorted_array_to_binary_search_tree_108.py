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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if n <= 0: return None
        mid = n // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    def get_list_len(self, head):
        size = 0
        while head != None:
            head = head.next
            size += 1
        return size

    def helper(self, head, size):
        if size == 0: return None, head
        l_size = size // 2
        left, cur = self.helper(head, l_size)
        root = TreeNode(cur.val)
        if cur != None:
            cur = cur.next
            root.right, cur = self.helper(cur, size - l_size -1)
        root.left = left
        return root, cur

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None: return None
        size = self.get_list_len(head)
        return self.helper(head, size)[0]



def show_tree(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        size = len(queue)
        level_res = []
        for i in range(size):
            node = queue[0]
            queue.pop(0)
            level_res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        print(level_res)


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
new_tree = s.sortedListToBST(head)
show_tree(new_tree)